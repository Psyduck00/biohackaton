import xml.etree.ElementTree as Xet
import pandas as pd

# id = Column(Integer, primary_key=True)
#     record_id = Column(Integer)
#     process_id = Column(String())
#     bin_url = Column(String())
#     sampleid = Column(String())
#     catalognum = Column(String())
#     fieldnum = Column(String())
#     institution_storing = Column(String())
#     identification_provided_by = Column(String())
#     phylum = Column(String())
#     class_name = Column(String())
#     order = Column(String())
#     voucher_status = Column(String())
#     reproduction = Column(String())
#     sex = Column(String())
#     lifestage = Column(String())
#     country = Column(String())
#     lat = Column(String())
#     lon = Column(String())
#     coord_source = Column(String())
#     coord_accuracy = Column(String())
#     sequenceID = Column(String())
#     markercode = Column(String())
#     nucleotides = Column(String())
#     notes = Column(String())

  
cols = ["record_id", "process_id", "bin_url", "sampleid", "catalognum", "fieldnum", "institution_storing", "identification_provided_by",
 "phylum", "class_name", "order", "voucher_status", "reproduction", 
"sex", "lifestage", "country", "lat", "lon", "coord_source", "coord_accuracy", "sequenceID", "markercode", "nucleotides", "notes"]
rows = []
  
# Parsing the XML file
xmlparse = Xet.parse('bold_data.xml')
root = xmlparse.getroot()
for i in root:
    record_id = i.find("record_id").text
    process_id = i.find("process_id").text
    bin_url = i.find("bin_url").text
    sampleid = i.find("sampleid").text
    catalognum = i.find("catalognum").text
    fieldnum = i.find("fieldnum").text
    institution_storing = i.find("institution_storing").text
    identification_provided_by = i.find("identification_provided_by").text
    phylum = i.find("phylum").text
    class_name = i.find("class_name").text
    order = i.find("order").text
    voucher_status = i.find("voucher_status").text
    reproduction = i.find("reproduction").text
    sex = i.find("sex").text
    lifestage = i.find("lifestage").text
    country = i.find("country").text
    lat = i.find("lat").text
    lon = i.find("lon").text
    coord_source = i.find("coord_source").text
    coord_accuracy = i.find("coord_accuracy").text
    sequenceID = i.find("sequenceID").text
    markercode = i.find("markercode").text
    nucleotides = i.find("nucleotides").text
    notes = i.find("notes").text
  
    rows.append({"record_id": record_id,
    "process_id": process_id,
    "bin_url": bin_url,
    "sampleid": sampleid,
    "catalognum": catalognum,
    "fieldnum": fieldnum,
    "institution_storing": institution_storing,
    "identification_provided_by": identification_provided_by,
    "phylum": phylum,
    "class_name": class_name,
    "order": order,
    "voucher_status": voucher_status,
    "reproduction": reproduction,
    "sex": sex,
    "lifestage": lifestage,
    "country": country,
    "lat": lat,
    "lon": lon,
    "coord_source": coord_source,
    "coord_accuracy": coord_accuracy,
    "sequenceID": sequenceID,
    "markercode": markercode,
    "nucleotides": nucleotides,
    "notes": notes})
  
df = pd.DataFrame(rows, columns=cols)
  
# Writing dataframe to csv
df.to_csv('output.csv')