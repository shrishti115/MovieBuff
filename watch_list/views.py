# from django.shortcuts import render
# from watch_list.models import Movie


# from django.http import JsonResponse
# # Create your views here.
# def movie_list(request):
#     movies= Movie.objects.all()
#     data={
#         'movies' :list(movies.values())
        
#     }
#     return JsonResponse(data)
# def movie_details(request, pk):
#     movie= Movie.objects.get(pk=pk)
#     print(movie)