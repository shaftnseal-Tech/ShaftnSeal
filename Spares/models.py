from django.db import models

# Maker Table
import uuid
from django.db import models

# Maker Table
class PumpMaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Maker Name")

    def __str__(self):
        return self.name


# Pump Model Table
class PumpModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    maker = models.ForeignKey(PumpMaker, on_delete=models.CASCADE, related_name='pump_models')
    name = models.CharField(max_length=100, verbose_name="Model Name")

    def __str__(self):
        return f"{self.maker.name} - {self.name}"


# Variant Table
class PumpModelVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(PumpModel, on_delete=models.CASCADE, related_name='variants')
    discharge_diameter = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Discharge Diameter (mm)")
    stages = models.IntegerField(verbose_name="Number of Stages")

    def __str__(self):
        return f"{self.model.name} - {self.discharge_diameter}mm - {self.stages} stages"


class PumpModelDesign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_design = models.CharField(max_length=100, verbose_name="Model Design")
    varient = models.ForeignKey(PumpModelVariant, on_delete=models.CASCADE, related_name='designs')
    
    def __str__(self):
        return f"{self.varient.model.name} - {self.model_design}"
# Parts Table
class PumpParts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    part_no = models.CharField(max_length=50, verbose_name="Part Number")
    name = models.CharField(max_length=100, verbose_name="Part Name")
    technical_details = models.FileField(upload_to='technical_files', blank=True, null=True, verbose_name="Technical Details")
    drawing_file = models.FileField(upload_to='drawings/', blank=True, null=True, verbose_name="Drawing File")
    cad_file = models.FileField(upload_to='cad_files/', blank=True, null=True, verbose_name="CAD File")
    mapping = models.FileField(upload_to='mapping_files/', blank=True, null=True, verbose_name="Mapping File")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.part_no} - {self.name}"
    


class Materials(models.Model):
    material_name = models.CharField(max_length=100, verbose_name="Material Name")
    material_description = models.FileField(upload_to='material_descriptions/', blank=True, null=True, verbose_name="Material Description")

    
    def __str__(self):
        return self.material_name
    
class PartMaterials(models.Model):
    part = models.ForeignKey(PumpParts, on_delete=models.CASCADE, related_name='materials')
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, related_name='parts')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    available = models.IntegerField(default=True, verbose_name='Available Quantity')
    class Meta:
        constraints= [
            models.UniqueConstraint(fields=['part', 'materials'], name='unique_part_materials')
        ]
    def __str__(self):
       return f"{self.part.part_no} - {self.materials.material_name} (Rs{self.price})"

# Mapping parts to Variants
class ModelVariantPart(models.Model):
    variant = models.ForeignKey(PumpModelVariant, on_delete=models.CASCADE, related_name='variant_parts')
    variant_part_materials = models.ForeignKey(PartMaterials, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['variant', 'variant_part_materials'], name='unique_variant_part')
        ]

    def __str__(self):
        return (
            f"Variant {self.variant} -> "
            f"Part {self.variant_part_materials.part.part_no} - "
            f"{self.variant_part_materials.part.name} - "
            f"{self.variant_part_materials.materials.material_name}"
        )

class ModelVarientDesignParts(models.Model):
    design = models.ForeignKey(PumpModelDesign, on_delete=models.CASCADE, related_name='design_parts')
    design_parts_materials = models.ForeignKey(PartMaterials, on_delete=models.CASCADE , related_name='design_parts')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['design', 'design_parts_materials'], name='unique_design_part')
        ]
    def __str__(self):
        return f"Design {self.design} -> Part {self.design_parts_materials.part.part_no} - {self.design_parts_materials.part.name} - {self.design_parts_materials.materials.material_name}"

class ModelPart(models.Model):
    model = models.ForeignKey(PumpModel, on_delete=models.CASCADE, related_name='common_parts')
    part_materials = models.ForeignKey(PartMaterials, on_delete=models.CASCADE)
    
    
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['model', 'part_materials'], name='unique_model_part')
        ]
    def __str__(self):
        return f"Common Part for {self.model}: {self.part_materials.part.part_no} - {self.part_materials.part.name} - {self.part_materials.materials.material_name}"


   