#!/usr/bin/python
# coding: UTF-8
# ver1.21115
# (C) 2012 Matsuda Hiroaki

import csv
import ConfigParser as Conf

class CsvReader(object):
    def __init__(self, inifile):
        self.conf = Conf.SafeConfigParser()
        self.conf.read(inifile)
        csv_num = int(self.conf.get('CSV', 'csvfilenum'))
        self.delimiter = self.conf.get('CSV', 'delimiter')
        self.data_type = self.conf.get('CSV', 'data_type')
        self.csv_path = []
        for i in range(csv_num):
            self.csv_path.append(self.conf.get('CSV', 'csv_' + str(i + 1)))
        
    def read_csv(self, path):
        csvfile = open(path, 'rb')

        csv_data = []
        for row in csv.reader(csvfile, delimiter = self.delimiter):
            csv_data.append(self._change_type(row))

        csvfile.close()
                
        return csv_data

    def get_csv_path(self):
        return self.csv_path
        
    def _change_type(self, list):
        for i in range(len(list)):
            if self.data_type == 'short':
                list[i] = int(list[i])
            
            elif self.data_type == 'long':
                list[i] = long(list[i])

            elif self.data_type == 'float':
                list[i] = float(list[i])
                        
            elif self.data_type == 'double':
                list[i] = float(list[i])
                
            elif self.data_type == 'char':
                list[i] = int(list[i])
                    
            elif self.data_type == 'string':
                list[i] = str(list[i])
                
            elif self.data_type == 'bool':
                list[i] = bool(list[i])
                
            elif self.data_type == 'octet':
                list[i] = int(list[i])

        return list

if __name__ == '__main__':
    csvfile = CsvReader('ini/multitypeconsolein.ini')

    path = csvfile.get_csv_path()
    print path
    
    csv_list = []
    for filepath in path:
        csv_list.append(csvfile.read_csv(filepath))

    print 'csv_1'
    print csv_list[0]
    print 'csv_2'
    print csv_list[1]
