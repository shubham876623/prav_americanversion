from . models import Product
from rest_framework import serializers
class Productserializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model=Product
        fields = '__all__'
    def create(self, validated_data):
        title ,price,model_number,prodcut_url,product_image_url,created_at,brand,rating,categories=validated_data.get('title'),validated_data.get('price'),validated_data.get('model_number'),validated_data.get('prodcut_url'),validated_data.get('product_image_url'),validated_data.get('created_at'),validated_data.get('brand'),validated_data.get('rating'),validated_data.get('categories')
        
        print(model_number,created_at,"ttttttttttttttttttttttttttttttttttttttt")
        product_objs = Product.objects.filter(model_number=model_number)
        if product_objs.exists():
            
            product_obj = product_objs.first()
            # print(product_obj,"ttttttttttttttttttttttttttttttttttttttt")
            pre_saved_model_number = getattr(product_obj,'model_number')
            if pre_saved_model_number==model_number:
                   print(pre_saved_model_number,"pppppppppppppppppppppppppppppppppppp")
                   product_objs.update(title=title,price=price,model_number=model_number,prodcut_url=prodcut_url,product_image_url=product_image_url,brand=brand,rating=rating,categories=categories,created_at=created_at)
        
        else:
            product_obj= Product.objects.create(title=title,price=price,model_number=model_number,prodcut_url=prodcut_url,product_image_url=product_image_url,brand=brand,rating=rating,categories=categories,created_at=created_at)
    
    
    
        return product_obj
    # except Exception as e:
    #     raise serializers.ValidationError({
    #         "errors":str(e)
    #     })

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
