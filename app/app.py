from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import xml.etree.ElementTree as Xet
from connection_management import DBConncectionManager
from models import Records
import pandas as pd
from result_schema import ResultItemResponseSchema
import math
import json
app = Flask(__name__)

records_schema = ResultItemResponseSchema(many=True)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/xml", methods=['GET','POST'])
def parse():

    dataframe1 = pd.read_excel('bold_data.xlsx')
    print(dataframe1)

    upper_range = len(dataframe1)
    print(upper_range)

    for row in range(0, (upper_range)):
        with DBConncectionManager() as db_session:
            geo=[]
            lon = dataframe1['lon'][row]
            lat = dataframe1['lat'][row]

            point = {}
            if lat is not None:
              point["lat"]= round(lat, 3)
              point["lat"] = format(point["lat"], '.3f')
              print(point["lat"])
              print('if')
            else:
              point["lat"]= lat
              print('else')


            if lon is not None:
              point["lon"]= round(lon, 3)
              point["lon"] = format(point["lon"], '.3f')
            else:
              point["lon"]= lon
            geo.append(point)
            print (geo)
            print(geo[0])

      
            add_items = Records(
                        record_id = int(dataframe1['recordID'][row]),
                        process_id = dataframe1['processid'][row],
                        bin_url = dataframe1['bin_uri'][row],
                        sampleid = dataframe1['sampleid'][row],
                        catalognum = dataframe1['catalognum'][row],
                        fieldnum = dataframe1['fieldnum'][row],
                        institution_storing = dataframe1['institution_storing'][row],
                        identification_provided_by = dataframe1['identification_provided_by'][row],
                        phylum = dataframe1['phylum_name'][row],
                        class_name = dataframe1['class_name'][row],
                        order_name = dataframe1['order_name'][row],
                        voucher_status = dataframe1['voucher_status'][row],
                        reproduction = dataframe1['reproduction'][row],
                        sex = dataframe1['sex'][row],
                        lifestage = dataframe1['lifestage'][row],
                        country = dataframe1['country'][row],
                        lat = dataframe1['lat'][row],
                        lon = dataframe1['lon'][row],
                        coord_source = dataframe1['coord_source'][row],
                        coord_accuracy = dataframe1['coord_accuracy'][row],
                        sequenceid = dataframe1['sequenceID'][row],
                        markercode = dataframe1['markercode'][row],
                        nucleotides = dataframe1['nucleotides'][row],
                        notes = dataframe1['notes'][row],
                        image_urls = dataframe1['image_urls'][row],
                        geo_location = str(geo[0])
                                            )

            db_session.add(add_items)
            print(add_items)
            db_session.commit()
  
    
    # cols = ["record_id", "process_id", "bin_url", "sampleid", "catalognum", "fieldnum", "institution_storing", "identification_provided_by",
    # "phylum", "class_name", "order", "voucher_status", "reproduction", 
    # "sex", "lifestage", "country", "lat", "lon", "coord_source", "coord_accuracy", "sequenceID", "markercode", "nucleotides", "notes"]
    # print(cols)
    # rows = []

    # # Parsing the XML file
    # xmlparse = Xet.parse('bold_data.xml')
    # root = xmlparse.getroot()
    # for i in root:
    #     print(i)
    #     record_id = i.find("record_id").text
    #     process_id = i.find("process_id").text
    #     bin_url = i.find("bin_url").text
    #     sampleid = i.find("sampleid").text
    #     catalognum = i.find("catalognum").text
    #     fieldnum = i.find("fieldnum").text
    #     institution_storing = i.find("institution_storing").text
    #     identification_provided_by = i.find("identification_provided_by").text
    #     phylum = i.find("phylum").text
    #     class_name = i.find("class_name").text
    #     order = i.find("order").text
    #     voucher_status = i.find("voucher_status").text
    #     reproduction = i.find("reproduction").text
    #     sex = i.find("sex").text
    #     lifestage = i.find("lifestage").text
    #     country = i.find("country").text
    #     lat = i.find("lat").text
    #     lon = i.find("lon").text
    #     coord_source = i.find("coord_source").text
    #     coord_accuracy = i.find("coord_accuracy").text
    #     sequenceID = i.find("sequenceID").text
    #     markercode = i.find("markercode").text
    #     nucleotides = i.find("nucleotides").text
    #     notes = i.find("notes").text

    # rows.append({"record_id": record_id,
    # "process_id": process_id,
    # "bin_url": bin_url,
    # "sampleid": sampleid,
    # "catalognum": catalognum,
    # "fieldnum": fieldnum,
    # "institution_storing": institution_storing,
    # "identification_provided_by": identification_provided_by,
    # "phylum": phylum,
    # "class_name": class_name,
    # "order": order,
    # "voucher_status": voucher_status,
    # "reproduction": reproduction,
    # "sex": sex,
    # "lifestage": lifestage,
    # "country": country,
    # "lat": lat,
    # "lon": lon,
    # "coord_source": coord_source,
    # "coord_accuracy": coord_accuracy,
    # "sequenceID": sequenceID,
    # "markercode": markercode,
    # "nucleotides": nucleotides,
    # "notes": notes})

    # df = pd.DataFrame(rows, columns=cols)

    # # Writing dataframe to csv
    # df.to_csv('output.csv')


    return 'done'

@app.route("/get-specimen-details-by-location", methods=['GET'])
def get_location():
  with DBConncectionManager() as db_session:

    all_records = db_session.query(Records).filter(Records.lat != 'NaN').all()
    return jsonify(records_schema.dump(all_records))

import math

@app.route("/get", methods=['GET'])
def findpoints():

    lat = request.args.get('lat')
    lon = request.args.get('lon')
    lat = float(lat)
    lon = float(lon)

    radius = 1
    N = 360 

    # generate points
    circlePoints = []
    for k in range(N):
        angle = math.pi*2*k/N
        dx = radius*math.cos(angle)
        dy = radius*math.sin(angle)
        point = {}
        pain = "{'lat': 27.243, 'lon': 87.481}"
        #['lat']= lat + (180/math.pi)*(dy/6371) #Earth Radius
        point['lat']=float('%.3f' % (lat + (180/math.pi)*(dy/6371)))
        #point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        point['lon']= float('%.3f' % (lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180)))
        # point['lat']=float('%.4f' % (lat + (180/math.pi)*(dy/6371)))
        # #point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        # point['lon']= float('%.4f' % (lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180)))
        # point['lat']=float('%.5f' % (lat + (180/math.pi)*(dy/6371)))
        # #point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        # point['lon']= float('%.5f' % (lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180)))
        # add to list
        circlePoints.append(str(point))
        circlePoints.append(pain)
        
    print(circlePoints)

    with DBConncectionManager() as db_session:
      query = db_session.query(Records).filter(Records.geo_location.in_(circlePoints)).all()



    return jsonify(records_schema.dump(query))
    #return circlePoints


 

if __name__ == "__main__":
  app.run()