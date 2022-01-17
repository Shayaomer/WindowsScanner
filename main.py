from db import collection
from installed_softwares import InstalledSoftware
from xmlParser import CpeXmlParser
from matching_cve_cpe import MatcherCveCpe
from download_db import DownloadDb
import download_db
import socket


def execute():
    print('Initializing the scan & matching process...')
    print("Downloading CVE data...")
    DownloadDb()
    print("Downloading CPE data...")
    download_db.download_file()
    download_db.unzip_file('official-cpe-dictionary_v2.3.xml.zip', directory_to_extract=None)

    print('Getting installed softwares...')
    i_s = InstalledSoftware()
    i_s.dump_software_lst_to_json(["Publisher", 'DisplayVersion', 'DisplayName'])

    print('Parsing the CPE data...')
    b = CpeXmlParser('official-cpe-dictionary_v2.3.xml')
    b.csv_creator('official-cpe-dictionary_v2.3.xml')

    c = MatcherCveCpe()
    res_json = c.match_cve_cpe()
    return {'_id': socket.gethostname(),
            '_data': res_json}

# Run this to scan & upload to the mongoDB cloud database
# Scan result will also be saved at json_final_res.json
if __name__ == '__main__':
    c = execute()
    comp_name = str(socket.gethostname())
    if collection.find_one({'_id': comp_name}) == None:
        collection.insert_one(c)
    else:
        collection.delete_one({'_id': comp_name})
        collection.insert_one(c)