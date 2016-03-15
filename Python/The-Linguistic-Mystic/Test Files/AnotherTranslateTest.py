
#!/usr/bin/env python
# -*- coding: utf-16 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Translate.
Command-line application that translates some text.
"""
from __future__ import print_function

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from googleapiclient.discovery import build


def main():
  
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build('translate', 'v2',
            developerKey='AIzaSyBUQS5Uc1v8Iq8kTbSkhdnNPkF6icsBG3w')
  #print(service.languages().list(
#    ).execute())

  translator = (service.translations().list(
      source='en',
      target=i,
      q=[userRequestForTranslation]
    ).execute())
  translator = str(translator)
  i = 0
  translationStart = 0
  translationEnd = 0
  while i<(len(translator)-2):
    if(translator[i]==':'and translator[i+1]==' ' and translator[i+2]=='u'):
      translationStart = i+4
    i += 1
  j = 2
  while j<(len(translator)-2):
    if(translator[j]=='}'and translator[j+1]==']' and translator[j+2]=='}'):
      translationEnd = i-2
    j +=1
  print(translator[translationStart:translationEnd])

if __name__ == '__main__':
      main()
