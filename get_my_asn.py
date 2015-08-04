#!/usr/bin/python
# Aurthor : Edouard Fazenda <edouard.fazenda@gmail.com>
# Date : 04 August 2015
# Get my AS Number (Autonomous System) via http://www.whatismyasn.org

# The MIT License (MIT)
#
# Copyright (c) <2015> <edouard.fazenda@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import urllib2
import re
import argparse

def get_asn_detail(data):

   as_path_regex = re.compile('^Your\sAS\sPath\sto\sthis\ssite\swas:\s(.*$)')
   as_number_regex = re.compile('^Your\sorigin\sAS\sis:\s(.*$)')

   for line in data:
      value = re.sub('<[^>]*>', '', line)
      as_path = as_path_regex.match(value)
   
      if as_path is not None and as_path != "":
         print "[INFO] : The AS Path is : ", as_path.group(1)
   
      as_number = as_number_regex.match(value)

      if as_number is not None and as_number != "":
         print "[INFO] : The AS name and number is : ", as_number.group(1)

def verbose(response):
   
   print "---------------------------------------------------------------------"
   print "[DEBUG] HTTP Code : ", response.code
   print "[DEBUG] The Server is :", response.info()['server']
   print "[DEBUG] The Date is : ", response.info()['date']
   print "[DEBUG] The Content Type is : ", response.info()['content-type']
   print "[DEBUG] The Content Lenght is : ", response.info()['content-length']
   print "---------------------------------------------------------------------"
if __name__ == '__main__':

   response = urllib2.urlopen('http://www.whatismyasn.org',None,10)
   data = response.readlines()

   parser = argparse.ArgumentParser(description='Get Autonomous System Information')
   parser.add_argument('-v', '--verbose', action='store_true', help='Verbose Output')
   args = parser.parse_args()

   print "[INFO] : Getting data from : ", response.geturl(), "..."

   if args.verbose:
      verbose(response)
      get_asn_detail(data)
   else:
      get_asn_detail(data)

