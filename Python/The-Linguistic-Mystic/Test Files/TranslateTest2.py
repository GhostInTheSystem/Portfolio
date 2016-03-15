import urllib.request

#urllib.request.urlopen("https://www.googleapis.com/language/translate/v2?key=IAIzaSyBUQS5Uc1v8Iq8kTbSkhdnNPkF6icsBG3w&source=en&target=de&q=Hello%20world").read()

with urllib.request.urlopen('https://www.googleapis.com/language/translate/v2?key=IAIzaSyBUQS5Uc1v8Iq8kTbSkhdnNPkF6icsBG3w&source=en&target=de&q=Hello%20world') as response:
   html = response.read()
