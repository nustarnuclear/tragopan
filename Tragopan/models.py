from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


    
# base model to contain the basic information
class BaseModel(models.Model):
    time_inserted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True)
    class Meta:
        abstract=True

#################################################       
# Concrete models in accordance with the database
#################################################

#################################################
#basic information 
#################################################

#describe element information
class Element(BaseModel):
    atomic_number = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=8,unique=True)
    nameCH = models.CharField(max_length=8)
    nameEN = models.CharField(max_length=40)
    reference = models.CharField(max_length=80, default='IUPAC')
    
    class Meta:
        db_table='element'
        ordering=['atomic_number']
    def __str__(self):
        return self.symbol
    
class Nuclide(BaseModel):
    element = models.ForeignKey(Element,to_field="symbol",related_name='nuclides',related_query_name='nuclide')
    atom_mass = models.DecimalField(max_digits=9,decimal_places=6,validators=[MinValueValidator(0)])
    abundance = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text="unit:percentage")
    reference = models.CharField(max_length=80, default='IUPAC') 
    class Meta:
        db_table='Nuclide'
        unique_together = ('element', 'atom_mass')
        order_with_respect_to='element'
        ordering=['element']
            
    def __str__(self):
        return str(self.element)+str(round(self.atom_mass))

#describe material information
class Material(BaseModel):
    nameCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    material_composition=models.ManyToManyField(Element,through='MaterialComposition')
    
    class Meta:
        db_table='Material'
    
    def __str__(self):
        return self.nameEN
    
class MaterialComposition(BaseModel):
    material=models.ForeignKey(Material,related_name='elements',related_query_name='element')
    element=models.ForeignKey(Element,to_field='symbol')
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text="unit:percentage")
    
    class Meta:
        db_table='material_composition'
        order_with_respect_to='material'
        ordering=['material']
        unique_together=('material','element')
    
    def __str__(self):
        return str(self.material)+' '+str(self.element)
    
class MaterialAttribute(BaseModel):
    material=models.OneToOneField(Material,related_name='attribute')
    density=models.DecimalField(max_digits=20, decimal_places=10,help_text='unit:g_per_cm3')
    heat_capacity=models.DecimalField(max_digits=20, decimal_places=10,help_text='J_per_kg_per_K',blank=True,null=True)
    thermal_conductivity=models.DecimalField(max_digits=20, decimal_places=10,help_text='W_per_m_per_K',blank=True,null=True)
    expansion_coefficient=models.DecimalField(max_digits=20, decimal_places=10,help_text='m_per_K',blank=True,null=True)
    code = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table='material_attribute'
        
    def __str__(self):
        return str(self.material)+"'s attribute"

class MaterialNuclide(BaseModel):
    '''only describe the non natural element composition in material'''
    material=models.ForeignKey(Material,related_name='nuclides',related_query_name='nuclide')
    nuclide=models.ForeignKey(Nuclide)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text="unit:percentage")
    
    class Meta:
        db_table='material_nuclide'
    
    def __str__(self):
        return str(self.material)+' '+str(self.nuclide)

class Vendor(BaseModel):
    TYPE_CHOICES=(
        ('Designer','Designer'),
        ('Manufacturer','Manufacturer'),
        ('Material','Material'),
    )
    nameCH=models.CharField(max_length=40)
    abbrCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    abbrEN=models.CharField(max_length=40)
    type=models.CharField(max_length=12, choices=TYPE_CHOICES,default='Designer')
    
    class Meta:
        db_table='vendor'
        
    def __str__(self):
        return self.abbrCH
    
#################################################
#nuclear power plant basic information 
#################################################

class Plant(BaseModel):
    nameCH=models.CharField(max_length=40)
    abbrCH=models.CharField(max_length=40)
    nameEN=models.CharField(max_length=40)
    abbrEN=models.CharField(max_length=40)
    
    class Meta:
        db_table='plant'
        
    def __str__(self):
        return self.abbrCH   
    
class ReactorModel(BaseModel):
    MODEL_CHOICES=(
        ('QNPC2','QNPC2'),
        ('QNPC1','QNPC1'),
        ('M310','M310'),
        ('CAP1000','CAP1000'),
        ('AP1000','AP1000'),
    )
    GENERATION_CHOICES = (
        ('2', '2'),
        ('2+', '2+'),
        ('3', '3'),
    )

    TYPE_CHOICES = (
        ('PWR', 'PWR'),
        ('BWR', 'BWR'),
    )

    GEOMETRY_CHOICES = (
        ('Cartesian', 'Cartesian'),
        ('Hexagonal', 'Hexagonal'),
    )
    
    SYMBOL_CHOICES = (
        ('Number', 'Number'),
        ('Letter', 'Letter'),
    )


    model = models.CharField(max_length=50,choices=MODEL_CHOICES)
    generation = models.CharField(max_length=2, choices=GENERATION_CHOICES)
    reactor_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    geometry_type = models.CharField(max_length=9, choices=GEOMETRY_CHOICES)
    row_symbol = models.CharField(max_length=6, choices=SYMBOL_CHOICES)
    column_symbol = models.CharField(max_length=6, choices=SYMBOL_CHOICES)
    num_loops = models.PositiveSmallIntegerField()
    num_control_rod_mechanisms = models.PositiveSmallIntegerField()
    core_equivalent_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    active_height= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    cold_state_assembly_pitch= models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)],help_text='unit:cm')
    hot_state_assembly_pitch = models.DecimalField(max_digits=7, decimal_places=4,validators=[MinValueValidator(0)],help_text='unit:cm')
    vendor = models.ForeignKey(Vendor)
    
    def limit_thermal_couple_position_choices(self):
        return {'reactor_model': self.model}
    
    def limit_incore_instrument_position_choices(self):
        return {'reactor_model': self.model}
    
    thermal_couple_position=models.ManyToManyField('ReactorPosition',related_name='thermal_couple_position',db_table='thermal_couple_map',blank=True,limit_choices_to=limit_thermal_couple_position_choices)
    incore_instrument_position=models.ManyToManyField('ReactorPosition',related_name='incore_instrument_position',db_table='incore_instrument_map',blank=True,limit_choices_to=limit_incore_instrument_position_choices)
   
    class Meta:
        db_table = 'reactor_model'
    
    def __str__(self):
        return str(self.model)     

class ReactorPosition(BaseModel):
    reactor_model=models.ForeignKey(ReactorModel,related_name='positions',related_query_name='position')
    row=models.PositiveSmallIntegerField()
    column=models.PositiveSmallIntegerField()
    
    class Meta:
        db_table='reactor_position'
        unique_together=('reactor_model','row','column')
        
    def __str__(self):
        rowSymbol=self.reactor_model.row_symbol
        columnSymbol=self.reactor_model.column_symbol
        #transform the number to letter
        if rowSymbol=='Letter':
            if self.row<=8:
                rowRpr=chr(self.row+64)
            else:
                rowRpr=chr(self.row+65)
        else:
            rowRpr=str(self.row).zfill(2)
        
        if columnSymbol=='Letter':
            if self.column<=8:
                rowRpr=chr(self.column+64)
            else:
                rowRpr=chr(self.column+65)
        else:
            columnRpr=str(self.column).zfill(2)
        
        return '{} {}{}'.format(self.reactor_model,rowRpr,columnRpr)

class CoreBarrel(BaseModel):
    reactor_model =models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_barrel'
        
    def __str__(self):
        return "{}'s core barrel".format(self.reactor_model)
        
class CoreUpperPlate(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:KG')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_upper_plate'
    
    def __str__(self):
        return "{}'s core upper plate".format(self.reactor_model)
    
class CoreLowerPlate(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:KG')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_lower_plate'
    
    def __str__(self):
        return "{}'s core lower plate".format(self.reactor_model)
        
    
class ThermalShield(BaseModel):
    reactor_model=models.ForeignKey(ReactorModel)
    height =models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm') 
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    angle=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0),MaxValueValidator(360)],help_text='unit:degree')
    loc_height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    loc_theta=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0),MaxValueValidator(360)],help_text='unit:degree')
    gap_to_barrel=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='thermal_shield'
    
    def __str__(self):
        return "{}'s {} thermal shield".format(self.reactor_model, self.id)
    
class PressureVessel(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    weld_thickness = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    base_material = models.ForeignKey(Material,related_name='pressure_vessel_base')
    weld_material = models.ForeignKey(Material,related_name='pressure_vessel_weld')
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='pressure_vessel'
    
    def __str__(self):
        return "{}'s pressure vessel".format(self.reactor_model)

class PressureVesselInsulation(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    outer_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='pressure_vessel_insulation'
    
    def __str__(self):
        return "{}'s pressure vessel insulation".format(self.reactor_model)
    
class CoreBaffle(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    gap_to_fuel=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    outer_diameter=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material = models.ForeignKey(Material)
    thickness= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:KG',blank=True,null=True)
    vendor = models.ForeignKey(Vendor)
    class Meta:
        db_table='core_baffle'
    
    def __str__(self):
        return "{}'s core baffle".format(self.reactor_model)

#rip plate table is associate with core baffle table    
class RipPlate(BaseModel):
    core_baffle=models.OneToOneField(ReactorModel)
    height=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    thickness=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    width= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm',blank=True,null=True)
    material = models.ForeignKey(Material)
    
    class Meta:
        db_table='rip_plate'
    
    def __str__(self):
        return "{}'s rip plate".format(self.core_baffle)


    
    
        
    