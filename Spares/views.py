from django.http import JsonResponse,Http404
from django.shortcuts import render, get_object_or_404
from .models import PumpMaker, PumpModel, PumpModelVariant, ModelPart, ModelVariantPart,PartMaterials,PumpModelDesign,ModelVarientDesignParts
from django.contrib.auth.decorators import login_required

def get_pumpmodels(request,id):
    pumpmodels = PumpModel.objects.filter(maker_id=id)
    data = list(pumpmodels.values('id', 'name'))
    return JsonResponse(data, safe=False)

def get_model_varient(request,id):
    variants = PumpModelVariant.objects.filter(model_id=id)
    data = list(variants.values('id', 'discharge_diameter', 'stages'))
    return JsonResponse(data, safe=False)

def get_model_design(request,id):
    
    designs = PumpModelDesign.objects.filter(varient_id=id)
    data = list(designs.values('id', 'model_design'))
    return JsonResponse(data, safe=False)


def get_parts(request, model_id, variant_id, design_id):
    try:
        model = PumpModel.objects.get(id=model_id)
        variant = PumpModelVariant.objects.get(id=variant_id)
        design = PumpModelDesign.objects.get(id=design_id)
    
        
        common_parts = ModelPart.objects.filter(model=model)
        variant_parts = ModelVariantPart.objects.filter(variant=variant)
        variant_design_parts = ModelVarientDesignParts.objects.filter(design=design)
        parts_data = []

        # Process common model-level parts
        for part_wrapper in common_parts:
            pm = part_wrapper.part_materials
            part = pm.part
            materials = PartMaterials.objects.filter(part=part)
            material_data = []
            for material in materials:
                material_data.append({
                    'material_name': material.materials.material_name,
                    'material_description': material.materials.material_description.url if material.materials.material_description else '',
                    'price': str(material.price),
                    'available': material.available
                })

            parts_data.append({
                'part_no': part.part_no,
                'name': part.name,
                'materials': material_data,  # Add materials with price and availability
                'technical_details': part.technical_details.url if part.technical_details else '',
                'drawing': part.drawing_file.url if part.drawing_file else '',
                'cad_file': part.cad_file.url if part.cad_file else '',
                'mapping': part.mapping.url if part.mapping else ''
            })

        # Process variant-specific parts
        for part_wrapper in variant_parts:
            pm = part_wrapper.variant_part_materials
            part = pm.part
            materials = PartMaterials.objects.filter(part=part)
            material_data = []
            for material in materials:
                material_data.append({
                    'material_name': material.materials.material_name,
                    'material_description': material.materials.material_description.url if material.materials.material_description else '',
                    'price': str(material.price),
                    'available': material.available
                })

            parts_data.append({
                'part_no': part.part_no,
                'name': part.name,
                'materials': material_data,  # Add materials with price and availability
                'technical_details': part.technical_details.url if part.technical_details else '',
                'drawing': part.drawing_file.url if part.drawing_file else '',
                'cad_file': part.cad_file.url if part.cad_file else '',
                'mapping': part.mapping.url if part.mapping else ''
            })
        
        for part_wrapper in variant_design_parts:
            pm = part_wrapper.design_parts_materials
            part = pm.part
            materials = PartMaterials.objects.filter(part=part)
            material_data = []
            for material in materials:
                material_data.append({
                    'material_name': material.materials.material_name,
                    'material_description': material.materials.material_description.url if material.materials.material_description else '',
                    'price': str(material.price),
                    'available': material.available
                })

            parts_data.append({
                'part_no': part.part_no,
                'name': part.name,
                'materials': material_data,  # Add materials with price and availability
                'technical_details': part.technical_details.url if part.technical_details else '',
                'drawing': part.drawing_file.url if part.drawing_file else '',
                'cad_file': part.cad_file.url if part.cad_file else '',
                'mapping': part.mapping.url if part.mapping else ''
            })
        # Render the HTML template with the parts data and model/variant details
        return render(request, 'Spares/Sparesparts.html', {
            
            'model': model,
            'variant': variant,
            'parts_data': parts_data
        })

    except PumpModel.DoesNotExist:
        raise Http404("Model not found")
    except PumpModelVariant.DoesNotExist:
        raise Http404("Variant not found")
    except Exception as e:
        raise Http404(f"Internal server error: {str(e)}")


@login_required
def maker_model(request):
    makers = PumpMaker.objects.all()
    return render(request, 'Spares/MakerModel.html', {'makers': makers})

