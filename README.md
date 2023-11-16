# Shiny-iCalendar-Generator
Single event use. Test deployment via shinylive

## Roadmap

- [X] Function to jointly  create datetime object from date input and select input shiny. dateobject + string
- [X] Sensible time dictionary like regular a.m to p.m time slots
- [ ] Add 30 mins increments
- [ ] Cooler QR output see [here](https://medium.com/@reegan_anne/fully-customizable-qr-codes-in-python-7eb8a7c3b0da)
- [X] How to center image and make sensible size ouput?
- [ ] Download QR image
- [ ] Download ics file
- [ ] Allow logo input to center
- [ ] Deploy github Pages

## Cloud Buildpack

 - Procfile not detected to run shiny

 - specifiy entrypoint in GOOGLE_ENTRYPOINT doesnt work

 - test with creating main.py ALONG WITH procfile WORKS!

 git clone https://github.com/dar4datascience/Shiny-iCalendar-Generator.git

 cd Shiny-iCalendar-Generator/

 pack build --builder=gcr.io/buildpacks/builder sample-shiny

 docker run -it -e PORT=8080 -p 8080:8080 sample-shiny

 pack build --builder=gcr.io/buildpacks/builder sample-shiny

 gcloud beta run deploy --source .
