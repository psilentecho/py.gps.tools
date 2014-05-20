import sys
import glob
import xml.etree.ElementTree as ET
import re

file_ext = 'gpx'

def get_log_fn():
    
    def log_fn(s):
        print(s)
        
    return log_fn

def load_all_gpx_files_in_folder(log_fn, folder_path):
    '''
    load all files with extension file_ext (gpx) in folder_path
    return dictionary with
    key = source file name with extension and path stripped, i.e. '/home/gps/dog.gpx' => 'dog'
    value = raw text file string
    '''
    
    gpx_file_texts = {}
    
    wildcard = '*.' + file_ext
    
    gpx_file_paths = glob.glob(folder_path + wildcard)
    
    for file_path in gpx_file_paths:
        with open(file_path, 'r') as gpx_file:
            raw_xml_text = gpx_file.read()
            
            file_name_with_ext = file_path.split('/')[-1]
            file_name = file_name_with_ext.replace('.' + file_ext, '')
                        
            gpx_file_texts[file_name] = raw_xml_text
    
    log_fn('%i raw %s files loaded' % (len(gpx_file_texts.keys()), file_ext))
    
    return gpx_file_texts

def load_xml(log_fn, raw_xml_by_label):
    '''
    discards badly formed xml
    '''    
    
    xml_by_label = {}
    
    badly_formed = []
    
    for label in raw_xml_by_label.keys():
        value = raw_xml_by_label[label]
        try:
            xml = ET.fromstring(value)
            xml_by_label[label] = xml
        except Exception as e:
            badly_formed.append(label)
    
    log_fn('%i valid xml' % len(xml_by_label.keys()))
    log_fn('%i badly formatted: %s' % (len(badly_formed), ','.join(badly_formed)))
    
    return xml_by_label

def partition_to_waypoints_and_tracks(log_fn, xml_by_label):
    '''
    returns (waypoints, tracks)
    '''
    waypoints = {}
    tracks = {}
    return (waypoints, tracks)
            
if __name__ == '__main__':    
    
    log_fn = get_log_fn()
   
    raw_xml_by_label = load_all_gpx_files_in_folder(log_fn, sys.argv[1])
    
    key = raw_xml_by_label.keys()[0]
    
    print('\n' + key)
        
    xml = raw_xml_by_label[key]
    print('\n' + xml)
    
    xml = re.sub(' xmlns="[^"]+"', '', xml, count=1)
    print('\n' + xml)
    
    # xml_by_label = load_xml(log_fn, raw_xml_by_label)
    
    
    