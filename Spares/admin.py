from django.contrib import admin
from django.utils.html import format_html
from .models import Maker, PumpModel, ModelVariant, Part, ModelVariantPart, ModelPart


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PumpModel)
class PumpModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'maker')
    list_filter = ('maker',)
    search_fields = ('name',)


@admin.register(ModelVariant)
class ModelVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'discharge_diameter', 'stages')
    list_filter = ('model',)
    search_fields = ('model__name',)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'part_no', 'name', 'material', 'created_at', 'updated_at',
                    )
    list_filter = ('material',)
    search_fields = ('part_no', 'name', 'material')
    readonly_fields = ('created_at', 'updated_at')

    # ➡️ Moved methods here!
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
    list_display = ('id', 'model', 'part')
    list_filter = ('model',)


@admin.register(ModelVariantPart)
class ModelVariantPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'part')
    search_fields = ('variant__model__name', 'part__name')
    list_filter = ('variant__model',)
