from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PumpMaker, PumpModel, PumpModelVariant,
    PumpParts, PartMaterials, ModelVariantPart, 
    ModelPart,Materials,PumpModelDesign,ModelVarientDesignParts
)


@admin.register(PumpMaker)
class PumpMakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PumpModel)
class PumpModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'maker')
    list_filter = ('maker',)
    search_fields = ('name',)


@admin.register(PumpModelVariant)
class PumpModelVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'discharge_diameter', 'stages')
    list_filter = ('model',)
    search_fields = ('model__name',)

@admin.register(PumpModelDesign)
class PumpModelDesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'varient', 'model_design')
    list_filter= ('varient',)
    search_fields = ('varient__model__name', 'model_design')


@admin.register(PumpParts)
class PumpPartsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'part_no', 'name', 'created_at', 'updated_at',
        'drawing_file_link', 'cad_file_link', 'mapping_file_link',
    )
    search_fields = ('part_no', 'name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)

    def drawing_file_link(self, obj):
        if obj.drawing_file:
            return format_html('<a href="{}" download>Download</a>', obj.drawing_file.url)
        return "No file"
    drawing_file_link.short_description = "Drawing File"

    def cad_file_link(self, obj):
        if obj.cad_file:
            return format_html('<a href="{}" download>Download</a>', obj.cad_file.url)
        return "No file"
    cad_file_link.short_description = "CAD File"

    def mapping_file_link(self, obj):
        if obj.mapping:
            return format_html('<a href="{}" download>Download</a>', obj.mapping.url)
        return "No file"
    mapping_file_link.short_description = "Mapping File"


@admin.register(ModelPart)
class ModelPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'get_part', 'get_material', 'get_price')
    list_filter = ('model',)
    search_fields = ('model__name', 'part_materials__part__name')

    def get_part(self, obj):
        return obj.part_materials.part.name
    get_part.short_description = "Part"

    def get_material(self, obj):
        return obj.part_materials.materials.material_name
    get_material.short_description = "Material"

    def get_price(self, obj):
        return obj.part_materials.price
    get_price.short_description = "Price"


@admin.register(ModelVariantPart)
class ModelVariantPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'get_part', 'get_material', 'get_price')
    list_filter = ('variant__model',)
    search_fields = ('variant__model__name', 'variant_part_materials__part__name')

    def get_part(self, obj):
        return obj.variant_part_materials.part.name
    get_part.short_description = "Part"

    def get_material(self, obj):
        return obj.variant_part_materials.materials.material_name
    get_material.short_description = "Material"

    def get_price(self, obj):
        return obj.variant_part_materials.price
    get_price.short_description = "Price"

@admin.register(ModelVarientDesignParts)
class ModelVarientDesignPartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'design', 'get_part', 'get_material', 'get_price')
    list_filter = ('design__varient__model',)
    search_fields = ('design__varient__model__name', 'design_parts_materials__part__name')
    def get_part(self, obj):
        return obj.design_parts_materials.part.name
    get_part.short_description = "Part"
    def get_material(self, obj):
        return obj.design_parts_materials.materials.material_name
    get_material.short_description = "Material"
    def get_price(self, obj):
        return obj.design_parts_materials.price
    get_price.short_description = "Price"

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_name','material_description')
    search_fields = ('material_name',)


@admin.register(PartMaterials)
class PartMaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'part', 'materials', 'price','available')
    list_filter = ('materials',)
    search_fields = ('part__name', 'materials__material_name')

