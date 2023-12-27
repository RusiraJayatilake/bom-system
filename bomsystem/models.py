from . import db

class BOM(db.Model):
    bom_id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_measure = db.Column(db.String, nullable=False)
    material = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    vendor_supplier = db.Column(db.String, nullable=False)
    lead_time = db.Column(db.Integer, nullable=False)
    revision_level = db.Column(db.String, nullable=False)
    assembly_code = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=False)
  
    # more attributes need to add futher
  
    def __init__(self, part_number, description=None, quantity=None, unit_measure=None,
                 material=None, weight=None, cost=None, vendor_supplier=None,
                 lead_time=None, revision_level=None, assembly_code=None, notes=None):
        self.part_number = part_number
        self.description = description
        self.quantity = quantity
        self.unit_measure = unit_measure
        self.material = material
        self.weight = weight
        self.cost = cost
        self.vendor_supplier = vendor_supplier
        self.lead_time = lead_time
        self.revision_level = revision_level
        self.assembly_code = assembly_code
        self.notes = notes