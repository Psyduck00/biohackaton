from base import Base
from sqlalchemy import Column, DateTime, Integer, String 
import uuid
from datetime import datetime
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import func

class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    record_id = Column(Integer)
    process_id = Column(String())
    bin_url = Column(String())
    sampleid = Column(String())
    catalognum = Column(String())
    fieldnum = Column(String())
    institution_storing = Column(String())
    identification_provided_by = Column(String())
    phylum = Column(String())
    class_name = Column(String())
    order_name = Column(String())
    voucher_status = Column(String())
    reproduction = Column(String())
    sex = Column(String())
    lifestage = Column(String())
    country = Column(String())
    lat = Column(String())
    lon = Column(String())
    coord_source = Column(String())
    coord_accuracy = Column(String())
    sequenceid = Column(String())
    markercode = Column(String())
    nucleotides = Column(String())
    notes = Column(String())
    image_urls = Column(String())
    geo_location = Column(String())


    def __init__(self, **kwargs):
        super(Records, self).__init__(**kwargs)

