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
        db_table='MaterialComposition'
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
        db_table='MaterialAttribute'
        
    def __str__(self):
        return str(self.material)+"'s attribute"

class MaterialNuclide(BaseModel):
    '''only describe the non natural element composition in material'''
    material=models.ForeignKey(Material,related_name='nuclides',related_query_name='nuclide')
    nuclide=models.ForeignKey(Nuclide)
    weight_percent=models.DecimalField(max_digits=9, decimal_places=6,validators=[MaxValueValidator(100),MinValueValidator(0)],help_text="unit:percentage")
    
    class Meta:
        db_table='MaterialNuclide'
    
    def __str__(self):
        return str(self.material)+' '+str(self.nuclide)
            
    