from django.contrib import admin
from .models import *
from django.db.models import Sum,F,Count
from _ast import Num
# Register your models here.

#################################################
#basic information 
#################################################

#element information

class NuclideInline(admin.TabularInline):
    model=Nuclide
    extra=0
    exclude=('reference','remark')
    readonly_fields=('atom_mass','abundance')
    
class ElementAdmin(admin.ModelAdmin):
    fieldsets=[
               (None,{'fields':['symbol']}),
               ('Element information',{'fields':['nameCH','nameEN'],'classes': ['collapse']})
             ]
    inlines=[NuclideInline]
    search_fields=('=symbol',)
    readonly_fields=('atomic_number','symbol','nameCH','nameEN')
    list_display=('atomic_number','symbol','nameCH','nameEN','element_average_mass','get_isotopes_num','is_correct')
    list_display_links=('atomic_number','symbol','nameCH','nameEN')
    
    #calculate the average mass of each element
    def element_average_mass(self,obj):
        element_mass=obj.nuclides.all().aggregate(avg_mass=Sum(F('atom_mass')*F('abundance')/100))
        if element_mass['avg_mass']==0:
            return 'Non Existent in nature'
        return str(round(element_mass['avg_mass'],5))       
    element_average_mass.short_description='Element Mass'
    
    #get the natural existent isotopes number of each element
    def get_isotopes_num(self,obj):
        isotopes=obj.nuclides.filter(abundance__gt=0).aggregate(num_isotopes=Count('id'))
        return isotopes['num_isotopes']
    get_isotopes_num.short_description='Natural Existent Isotopes Count'
    
    #check if satisfy the integrity constraint
    def is_correct(self,obj):
        pecentage_sum=obj.nuclides.all().aggregate(sum=Sum('abundance'))
        if pecentage_sum['sum'] in [100,0]:
            return True
        return False
    is_correct.short_description='Data Integrity?'
    is_correct.boolean=True       
admin.site.register(Element, ElementAdmin)

class NuclideAdmin(admin.ModelAdmin):
    exclude=('reference','remark')
    search_fields=('=element__symbol',)
    ordering=('element','atom_mass')
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('element','atom_mass','abundance')
        return ()    
admin.site.register(Nuclide, NuclideAdmin)

#material information
class MaterialCompositionInline(admin.TabularInline):
    model=MaterialComposition
    exclude=('remark',)
    
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra-1
        return extra
    #to control the non superuser have no right to edit
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('element','weight_percent')
        return ()
            

class MaterialAttributeInline(admin.TabularInline):
    model=MaterialAttribute
    extra=1
    exclude=('remark',)
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('density','heat_capacity','thermal_conductivity','expansion_coefficient','code')
        return ()
   
class MaterialNuclideInline(admin.TabularInline):
    model=MaterialNuclide
    extra=1
    exclude=('remark',)
    raw_id_fields=('nuclide',)
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('nuclide','weight_percent')
        return ()

    
class MaterialAdmin(admin.ModelAdmin):
    inlines=(MaterialCompositionInline,MaterialAttributeInline,MaterialNuclideInline)
    exclude=('remark',)
    list_display=('nameEN','nameCH','is_correct')
    list_display_links=('nameEN','nameCH')
    
    #check if satisfy the integrity constraint
    def is_correct(self,obj):
        pecentage_sum=obj.elements.all().aggregate(sum=Sum('weight_percent'))
        if pecentage_sum['sum']==100:
            return True
        return False
    is_correct.short_description='Data Integrity?'
    is_correct.boolean=True
    
    def get_readonly_fields(self,request, obj=None):
        if not request.user.is_superuser:
            return ('nameEN','nameCH')
        return ()
admin.site.register(Material, MaterialAdmin)

class VendorAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('nameEN','nameCH','type')
    list_display_links=('nameEN','nameCH')
admin.site.register(Vendor, VendorAdmin)

#################################################
#nuclear power plant basic information 
#################################################

class PlantAdmin(admin.ModelAdmin):
    exclude=('remark',)
    list_display=('nameEN','nameCH')
    list_display_links=('nameEN','nameCH')
admin.site.register(Plant, PlantAdmin)

class ReactorPositionAdmin(admin.ModelAdmin):
    exclude=('remark',)
    search_fields=('=row','=column')
    list_filter=('reactor_model__model',)
    list_display=('__str__','reactor_model')
    list_per_page=200
    ordering=('row','column')
admin.site.register(ReactorPosition, ReactorPositionAdmin)

#the following inline tables describe a kind of reactor model
class ReactorPositionInline(admin.TabularInline):
    model=ReactorPosition
    def get_extra(self, request, obj=None, **kwargs):
        extra = 121
        if obj:
            extra -= obj.positions.count()
        return extra
    exclude=('remark',)

class CoreBarrelInline(admin.TabularInline):
    model=CoreBarrel
    extra=1
    exclude=('remark',)
    verbose_name_plural='core barrel'
    
class CoreUpperPlateInline(admin.TabularInline):
    model=CoreUpperPlate
    extra=1
    exclude=('remark',)
    verbose_name_plural='core upper plate'
    
class CoreLowerPlateInline(admin.TabularInline):
    model=CoreLowerPlate
    extra=1
    exclude=('remark',)
    verbose_name_plural='core lower plate'
    
class ThermalShieldInline(admin.TabularInline):
    model=ThermalShield
    extra=1
    exclude=('remark',)

class PressureVesselInline(admin.TabularInline):
    model=PressureVessel
    extra=1
    exclude=('remark',)
    verbose_name_plural='pressure vessel'
    
class PressureVesselInsulationInline(admin.TabularInline):
    model=PressureVesselInsulation
    extra=1
    exclude=('remark',)
    verbose_name_plural='pressure vessel insulation'
    
class CoreBaffleInline(admin.TabularInline):
    model=CoreBaffle
    extra=1
    exclude=('remark',)
    verbose_name_plural='core baffle'

class ThermalCouplePositionInline(admin.TabularInline):
    model = ReactorModel.thermal_couple_position.through
    def get_extra(self, request, obj=None, **kwargs):
        extra =30
        if obj:
            extra -= obj.thermal_couple_position.count()
        return extra
    verbose_name='thermal_couple_position'
    verbose_name_plural='thermal couple position'

class IncoreInstrumentPositionInline(admin.TabularInline):
    model = ReactorModel.incore_instrument_position.through
    def get_extra(self, request, obj=None, **kwargs):
        extra =38
        if obj:
            extra -= obj.incore_instrument_position.count()
        return extra
    verbose_name='incore_instrument_position'
    verbose_name_plural='incore instrument position'
    
class ReactorModelAdmin(admin.ModelAdmin):
    exclude=('remark','thermal_couple_position','incore_instrument_position')
    #raw_id_fields=('thermal_couple_position','incore_instrument_position')
    inlines=[CoreBaffleInline,CoreUpperPlateInline,CoreLowerPlateInline,ThermalShieldInline,PressureVesselInline,PressureVesselInsulationInline,CoreBaffleInline,
             ThermalCouplePositionInline,IncoreInstrumentPositionInline,ReactorPositionInline]
    
    list_display=['model','generation','reactor_type','geometry_type','num_loops','num_control_rod_mechanisms',
                  'get_thermal_couple_num','get_incore_instrument_num','get_fuel_assembly_num']
    
    def get_thermal_couple_num(self,obj):
        num=obj.thermal_couple_position.count()
        return num
    get_thermal_couple_num.short_description='thermal couple count'
    
    def get_incore_instrument_num(self,obj):
        num=obj.incore_instrument_position.count()
        return num
    get_incore_instrument_num.short_description='incore instrument count'
    
    def get_fuel_assembly_num(self,obj):
        num=obj.positions.count()
        return num
    get_fuel_assembly_num.short_description='fuel assembly count'
        
admin.site.register(ReactorModel,ReactorModelAdmin)
    

