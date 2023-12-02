from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins,viewsets
from rest_framework.decorators import api_view,APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(http_method_names=["GET","POST"])
def list_products(request:Request):

    if(request.method=="POST"):
        data= request.data
        serializer = PostSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            res= {
                "message":"posts has been created",
                "data": serializer.data
            }
            return Response(data=res,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    posts= Post.objects.all()
    serializer = PostSerializer(instance=posts,many=True)
    res={
        "message":"posts",
        "data":serializer.data
    }
    return Response(data=res,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request:Request, post_id:int):
    post=get_object_or_404(Post,pk=post_id)
    serializer = PostSerializer(instance=post)
    res={
        "message":"post",
        "data":serializer.data
    }
   
    return Response(data=res,status=status.HTTP_200_OK)
    # return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['PUT'])
def update_post(request:Request, post_id:int):
    post=get_object_or_404(Post,pk=post_id)
    
    data= request.data

    serializer = PostSerializer(instance=post,data=data)

    if serializer.is_valid():
        serializer.save()

        res={
            "message":"post is updated successfully",
            "data":serializer.data
        }
        return Response(data=res,status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['DELETE'])
def delete_post(request:Request, post_id:int):
    post=get_object_or_404(Post,pk=post_id)
    post.delete()
    res={
        "message":"post is deleted successfully"
    }
    return Response(data=res,status=status.HTTP_204_NO_CONTENT)



# class PostListCreateView(APIView):

#     """
#     A View for creating and listing Posts
#     """


#     serializer_class = PostSerializer

#     def get(self,request:Request,*args, **kwargs):
#         posts= Post.objects.all()
#         serializer = self.serializer_class(instance=posts,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     def post(self,request:Request,*args, **kwargs):
#         data=request.data
#         serailizer = self.serializer_class(data=data)
#         if serailizer.is_valid():
#             serailizer.save()
#             return Response(data=serailizer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#  class PostReadUpdateDeleteView(APIView):
    """
    A View Reading updating deleting post
    """
    serializer_class=PostSerializer

    def get(self,request:Request,post_id:int,*args, **kwargs):
        post = get_object_or_404(Post,pk=post_id)
        serializer = self.serializer_class(instance=post)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request:Request,post_id:int,*args, **kwargs):
        post = get_object_or_404(Post,pk=post_id)
        data= request.data
        serializer = self.serializer_class(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request:Request,post_id:int,*args, **kwargs):
        post = get_object_or_404(Post,pk=post_id)
        post.delete()
        res={
            "message":"Post deleted successfully"
        }
        return Response(data=res,status=status.HTTP_200_OK)

class PostListCreateView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):

    """
    A generic View for creating and listing Posts
    """


    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request:Request,*args, **kwargs):
       return self.list(request,*args,**kwargs)

    def post(self,request:Request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    

class PostReadUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    """
    A View Reading updating deleting post
    """
    serializer_class=PostSerializer
    queryset= Post.objects.all()

    def get(self,request:Request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request:Request,*args, **kwargs):
        return self.update(request,*args, **kwargs)


    def delete(self,request:Request,*args, **kwargs):
       return self.destroy(request,*args, **kwargs)
    

class PostViewSet(viewsets.ViewSet):
    
    
    def list(self,request:Request):
        queryset= Post.objects.all()
        serializer = PostSerializer(instance=queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
        