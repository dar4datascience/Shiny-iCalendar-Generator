# The shinyswatch package provides themes from https://bootswatch.com/
import asyncio
import io
from datetime import date
from pathlib import Path
from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
import pytz
import qrcode
import tempfile

import shinyswatch
from shiny import App, Inputs, Outputs, Session, render, reactive, ui
from shiny.types import ImgData
import ipywidgets as widgets
from ical_2_qr import create_event_qr
from adhoc_datetime_maker import make_datetime

import os

firebase_api_key = os.getenv('firebase_api_key')

google_firebase_auth_js = f"""
    var config = {{
        apiKey: "{firebase_api_key}",
        authDomain: "shiny-buildpack-demo.firebaseapp.com",
    }};
    firebase.initializeApp(config);
"""

# A card component wrapper.
def ui_card(title, *args):
    return (
        ui.div(
            {"class": "card mb-4"},
            ui.div(title, class_="card-header"),
            ui.div({"class": "card-body"}, *args),
        ),
    )

# Time dictionary in the form of 1 PM, 2 PM, 3 PM, etc. all strings/
time_dictionary = {"1 PM": "1 PM",
                     "2 PM": "2 PM",
                     "3 PM": "3 PM",
                     "4 PM": "4 PM",
                     "5 PM": "5 PM",
                     "6 PM": "6 PM",
                     "7 PM": "7 PM",
                     "8 PM": "8 PM",
                     "9 PM": "9 PM",
                     "10 PM": "10 PM",
                     "11 PM": "11 PM",
                     "12 PM": "12 PM",
                     "1 AM": "1 AM",
                     "2 AM": "2 AM",
                     "3 AM": "3 AM",
                     "4 AM": "4 AM",
                     "5 AM": "5 AM",
                     "6 AM": "6 AM",
                     "7 AM": "7 AM",
                     "8 AM": "8 AM",
                     "9 AM": "9 AM",
                     "10 AM": "10 AM",
                     "11 AM": "11 AM",
                     "12 AM": "12 AM"}


css_path = Path(__file__).parent / "www" / "styles.css"


app_ui = ui.page_navbar(
        # Available themes:
    #  cerulean, cosmo, cyborg, darkly, flatly, journal, litera, lumen, lux,
    #  materia, minty, morph, pulse, quartz, sandstone, simplex, sketchy, slate,
    #  solar, spacelab, superhero, united, vapor, yeti, zephyr
    #    ui.tags.head(
    #     ui.tags.link(rel="stylesheet", href="styles.css")
    # ),
   # ui.include_css(css_path),
       ui.head_content(ui.tags.title("Demo Shiny Python"),
                    # add JS for authentication
                    ui.tags.script(src="https://www.gstatic.com/firebasejs/8.0/firebase.js"),
                     ui.tags.script(google_firebase_auth_js),),
       shinyswatch.theme.cyborg(),
    ui.nav(
        "Make iCalendar Event",
        ui.layout_sidebar(
            ui.sidebar(
                                ui.tags.h5("Crea iCalendar Event:"),
                ui.input_date("date_event", "Date input"),
                ui.input_select("hora", "Hora del Evento", time_dictionary),
                ui.input_text("titulo", "Titulo del Evento:", "General"),
                ui.tags.h5("actionButton with CSS class:"),
                ui.input_action_button(
                    "action2", "Insert Random Cat", class_="btn-primary"
                ),
            ),
            ui.page_fillable(
                ui.navset_pill(
                    ui.nav(
                        "QR Code",
                                                                                  ui_card(
                        ui.tags.h4("Codigo QR del Evento:"),
                        ui.output_text("txt"),
                        ui.tags.br(), 
                        ui.div(
                            #align image center
                            {"style": "display: flex; justify-content: center"},
                        ui.output_image("image",
                                        width='50%'),
                                                                                  )
    ),
                    ),
                    ui.nav("Download image",
                               ui_card(
        "Download a pre-existing file, using its existing name on disk.",
        ui.download_button("download1",
                            "Download .png"),
    )
    ),
                    ui.nav("Download .ics",
                                                          ui_card(
        "Download a pre-existing file, using its existing name on disk.",
        ui.download_button("download2",
                            "Download .ics"),
    )
    ),
                )
            ),
        ),
    ),
    title="Shiny iCalendar",
)


def server(input: Inputs, output: Outputs, session: Session):
   
    @session.download()
    def download1():
        # This is the simplest case. The implementation simply returns the path to a
        # file on disk.
        path = Path(__file__).parent / "mtcars.csv"
        return str(path)
    
    @session.download()
    def download2():
        # This is the simplest case. The implementation simply returns the path to a
        # file on disk.
        path = Path(__file__).parent / "mtcars.csv"
        return str(path)

    @reactive.event(input.hora, input.titulo, input.date_event)
    def compose_qr_event():
        #start_time = datetime(2023, 1, 25, 8, 0, 0, tzinfo=pytz.utc)
        temp_file_name = create_event_qr(made_datetime(), input.titulo())
        return temp_file_name
    
    @output
    @render.image(delete_file=True)
    def image() -> ui.Tag:
        from pathlib import Path

        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / compose_qr_event()),
                        "width": "95%"}
        return img

    # @output
    # @render.image
    # def image():
    #     from pathlib import Path

    #     dir = Path(__file__).resolve().parent
    #     img: ImgData = {"src": str(dir / "animated_qrcode.gif"), "width": "500px"}
    #     return img
    
    # DATE TIME NOT AVAILABLE BUT DATE AND TIME ARE
    # date_picker = widgets.DatePicker(
    # description='Pick a Date',
    # disabled=False
    # )

    # # time picker not available
    # time_picker = widgets.TimePicker(
    # description='Pick a Time',
    # disabled=False
    # )

    # @output
    # @render_widget
    # def input_date():
    #     return date_picker
    
    # @output
    # @render_widget
    # def input_time():
    #     return time_picker

    @reactive.event(input.hora, input.date_event)
    def made_datetime():
        return make_datetime(input.date_event(), input.hora())
    
    @output
    @render.text
    def txt():
        return f"The value of the made_datetime is: {made_datetime()} and event title is {input.titulo()}"
    

www_dir = Path(__file__).parent / "www"
app = App(ui=app_ui, server=server, static_assets=www_dir)