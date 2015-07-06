from django.contrib import admin
from .models import *
from django.db.models import Sum,F,Count
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
    list_display=('nameEN','nameCH')
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

#the following inline tables are gonna describe a kind of reactor model
class ReactorPositionInline(admin.TabularInline):
    model=ReactorPosition
    extra=121
    exclude=('reference','remark')
    
class CoreBarrelInline(admin.TabularInline):
    model=CoreBarrel
    extra=1
    exclude=('reference','remark')
    
class CoreUpperPlateInline(admin.TabularInline):
    model=CoreUpperPlate
    extra=1
    exclude=('reference','remark')
    
class CoreLowerPlateInline(admin.TabularInline):
    model=CoreLowerPlate
    extra=1
    exclude=('reference','remark')
    
class ThermalShieldInline(admin.TabularInline):
    model=ThermalShield
    extra=1
    exclude=('reference','remark')

class PressureVesselInline(admin.TabularInline):
    model=PressureVessel
    extra=1
    exclude=('reference','remark')
    
class PressureVesselInsulationInline(admin.TabularInline):
    model=PressureVesselInsulation
    extra=1
    exclude=('reference','remark')
    
class CoreBaffleInline(admin.TabularInline):
    model=CoreBaffle
    extra=1
    exclude=('reference','remark')
    
class ReactorModelAdmin(admin.ModelAdmin):
    inlines=[CoreBaffleInline,CoreUpperPlateInline,CoreLowerPlateInline,ThermalShieldInline,PressureVesselInline,PressureVesselInsulationInline,CoreBaffleInline,ReactorPositionInline]
admin.site.register(ReactorModel,ReactorModelAdmin)
    

