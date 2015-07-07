from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from _mysql import NULL
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
    abundance = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
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
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    
    class Meta:
        db_table='material_composition'
        order_with_respect_to='material'
        ordering=['material']
        unique_together=('material','element')
    
    def __str__(self):
        return str(self.material)+' '+str(self.element)
    
class MaterialAttribute(BaseModel):
    material=models.OneToOneField(Material,related_name='attribute')
    density=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'unit:g/cm3')
    heat_capacity=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'J/kg*K',blank=True,null=True)
    thermal_conductivity=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'W/m*K',blank=True,null=True)
    expansion_coefficient=models.DecimalField(max_digits=15, decimal_places=5,help_text=r'm/K',blank=True,null=True)
    code = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table='material_attribute'
        
    def __str__(self):
        return str(self.material)+"'s attribute"

class MaterialNuclide(BaseModel):
    '''only describe the non natural element composition in material'''
    material=models.ForeignKey(Material,related_name='nuclides',related_query_name='nuclide')
    nuclide=models.ForeignKey(Nuclide)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    
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

#################################################
#nuclear power plant equipment information
#################################################

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
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg')
    material = models.ForeignKey(Material)
    vendor = models.ForeignKey(Vendor)
    
    class Meta:
        db_table='core_upper_plate'
    
    def __str__(self):
        return "{}'s core upper plate".format(self.reactor_model)
    
class CoreLowerPlate(BaseModel):
    reactor_model=models.OneToOneField(ReactorModel)
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg')
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
    weight=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:Kg',blank=True,null=True)
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


#################################################
#nuclear power plant operation information 
#################################################

class UnitParameter(BaseModel):
    plant = models.ForeignKey(Plant)
    unit = models.PositiveSmallIntegerField()
    reactor_model = models.ForeignKey(ReactorModel)
    electric_power = models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:MW')
    thermal_power = models.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:MW')
    heat_fraction_in_fuel = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    primary_system_pressure= models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:MPa')
    ave_linear_power_density= models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/m')
    ave_vol_power_density = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/L')
    ave_mass_power_density = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:KW/Kg (fuel)')
    best_estimated_cool_vol_flow_rate = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text=r'unit:m3/h')
    bypass_flow_fraction = models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text=r"unit:%")
    cold_state_cool_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HZP_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HFP_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    HFP_core_ave_cool_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K')
    mid_power_cool_inlet_temp = models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='unit:K', blank=True, null=True)
    
    class Meta:
        db_table = 'unit_parameter'
        unique_together = ('plant', 'unit')
    
    def __str__(self):
        return '{} unit{}'.format(self.plant, self.unit)
 
class Cycle(BaseModel):
    unit=models.ForeignKey(UnitParameter)
    cycle = models.PositiveSmallIntegerField()
    starting_date = models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')
    shutdown_date = models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')
    cycle_length = models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:EFPD') 
    num_unplanned_shutdowns = models.PositiveSmallIntegerField()
    num_periodical_tests = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'cycle'
        unique_together = ('cycle', 'unit')
        
    def __str__(self):
        return '{} cycle{}'.format(self.unit, self.cycle)
    
class FuelAssemblyLoadingPattern(BaseModel):
    ROTATION_DEGREE_CHOICES=(
        ('0','0'),
        ('90','90'),
        ('180','180'),
        ('270','270'),
    )
    cycle=models.ForeignKey(Cycle,related_name='fuel_assembly_positions')
    reactor_position=models.ForeignKey(ReactorPosition)
    fuel_assembly=models.ForeignKey('FuelAssemblyRepository')
    rotation_degree=models.CharField(max_length=3,choices=ROTATION_DEGREE_CHOICES,default='0')
    cycle_burnup=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='MWd/tU',blank=True,null=True)
    
    class Meta:
        db_table='fuel_assembly_loading_pattern'
        unique_together=('cycle','reactor_position')
        
    def __str__(self):
        return '{} {} {}'.format(self.cycle, self.reactor_position,self.fuel_assembly)


#################################################
#fuel assembly information 
#################################################  

class FuelAssemblyModel(BaseModel):
    MODEL_CHOICES=(
            ('AFA2G','AFA2G'),
            ('AFA3G','AFA3G'),
    )
    
    model=models.CharField(max_length=5,choices=MODEL_CHOICES)
    overall_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    side_length=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    pin_pitch=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    lower_gap=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    upper_gap=models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    guid_tube_map=models.ManyToManyField('FuelAssemblyPosition',related_name='guid_tube_map',db_table='guid_tube_map')
    grid_position=models.ManyToManyField('Grid',through='GridPosition',related_name='grid_position')
    licensed_max_discharge_BU =models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='MWd/tU',blank=True,null=True)
    licensed_pin_discharge_BU =models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='MWd/tU',blank=True,null=True)
    vendor=models.ForeignKey(Vendor)
    
    class Meta:
        db_table='fuel_assembly_model'
    
    def __str__(self):
        return self.model
    
class FuelAssemblyRepository(BaseModel):
    PN=models.CharField(max_length=50,unique=True)
    model=models.ForeignKey(FuelAssemblyModel)
    batch_number=models.PositiveSmallIntegerField()
    manufacturing_date=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')
    arrival_date=models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')
    plant=models.ForeignKey(Plant)
    vendor=models.ForeignKey(Vendor)
    availability=models.NullBooleanField(default='True',verbose_name='available now?')
    
    class Meta:
        db_table='fuel_assembly_repository'
        
    def __str__(self):
        return self.PN
    
    
    
class FuelAssemblyPosition(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel,related_name='positions',related_query_name='position')
    row=models.PositiveSmallIntegerField()
    column=models.PositiveSmallIntegerField()
    
    class Meta:
        db_table='fuel_assembly_position'
        unique_together=('fuel_assembly_model','row','column')
        
    def __str__(self):
        return '{} R{}C{}'.format(self.fuel_assembly_model, self.row,self.column)

class Grid(BaseModel):
    FUCTIONALITY_CHOICS=(
                ('blend','blend'),
                ('fix','fix'),
    )
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    model=models.CharField(max_length=40)
    sleeve_material=models.ForeignKey(Material,related_name='grid_sleeves',related_query_name='grid_sleeve')
    sleeve_weight=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='g')
    sleeve_thickness=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')
    spring_material=models.ForeignKey(Material,related_name='grid_springs',related_query_name='grid_spring')
    spring_weight=models.DecimalField(max_digits=15, decimal_places=5,validators=[MinValueValidator(0)],help_text='g')
    spring_thickness=models.DecimalField(max_digits=10, decimal_places=5,validators=[MinValueValidator(0)],help_text='cm')
    functionality=models.CharField(max_length=5,choices=FUCTIONALITY_CHOICS,default='fix')
    vendor=models.ForeignKey(Vendor)
    
    class Meta:
        db_table='grid'
    
    def __str__(self):
        return self.model

class GridPosition(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    grid=models.ForeignKey(Grid)
    height= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm') 
    
    class Meta:
        db_table='grid_position'
        
    def __str__(self):
        return '{} {}'.format(self.fuel_assembly_model, self.grid)   

class GuidTube(BaseModel):
    fuel_assembly_model=models.ForeignKey(FuelAssemblyModel)
    outer_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    inner_diameter= models.DecimalField(max_digits=7, decimal_places=3,validators=[MinValueValidator(0)],help_text='unit:cm')
    material=models.ForeignKey(Material)
    vendor=models.ForeignKey(Vendor)
    
    class Meta:
        db_table='guid_tube'
        
    def __str__(self):
        return "{}'s guid tube".format(self.fuel_assembly_model)