from django.http import Http404
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from movies.models import Movie
# Create your views here.

def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie_list.html', context)

def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)#get(title='')
    except Exception as e:
        print(e)
        raise Http404
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)

def movie_create(request):
    """ kino haqida ma'lumotlarni qo'shish uchun method """
    
    context = {}
    errors = {}
    data = {}
    
    if request.method == 'POST':
        print(f"\nREQUEST METHOD:{request.method}\n")
        print(request.POST)
        
        title = request.POST['title']
        print(title,"\n")
        released_year = request.POST['released_year']
        print(released_year, "\n")
        lan = request.POST['language']
        duration = request.POST['duration']
        print(f"\n\n{duration}\n\n")
        source_link = request.POST['source_link']
        type = request.POST['type']
        cat = request.POST['category_id']
        slug = request.POST.get('slug')
        ban = request.POST['banner']
        
        print("\n", request.POST['type'], "\n")
        
        if not title:
            errors['title'] = "Iltimos kino nomini kiriting"
        if not duration:
            errors['duration'] = "Iltimos kino davomiyligini kiriting"
        if not source_link:
            errors['source_link'] = "Iltimos kino linkini kiriting "
        if not (type in ['SERIES', 'SHOW', 'MOVIE', "TRAILER"]):
            errors['type'] = "Siz noto'g'ri variantni tanladingiz"
        if not slug:
            errors['slug'] = "Iltimos slug ni  kiriting"
        if not released_year:
            errors['released_year'] = "Iltimos kino yilini kiriting"
        
        print("ERRORS COUNT:", len(errors))
        print("\nERRORS DICTIONARY", errors)
        
        data = {
            'title': title,
            'released_year': released_year,
            'language': lan,
            'source_link': source_link,
            'duration': duration,
            'type': type,
            'category_id': cat,
            "banner": ban,
            'slug': slug,
             
        }
        
        if len(errors) == 0:
            new_movie = Movie(title=title,
                          language=lan,
                          duration=duration,
                          released_year=released_year,
                          source_link=source_link,
                          type=type,
                          category_id=cat,
                          banner=ban,
                          slug=slug)
            new_movie.save()
            return redirect("/movies/")
    
    context = {'errors': errors, 'data': data}
    return render(request, 'movie_create.html', context)


def movie_edit(request, movie_id): #edit/5
    context = {}
    data = {}
    
    if movie_id:
        print("MOVIE ID:", movie_id)
        movie = Movie.objects.get(id=movie_id)  
        data = {
                'title': movie.title,
                'released_year': movie.released_year,
                'language': movie.language,
                'source_link': movie.source_link,
                'duration': movie.duration,
                'type': movie.type,
                'category_id': movie.category_id,
                "banner": movie.banner,
                'slug': movie.slug           
            }   
        print(movie.title)
        context = {'data': data}
        # return render(request, "movie_edit.html", context)
    
    if request.method == 'POST': 
        print(f"\nREQUEST METHOD : {request.method}\n")
        print(request.POST)
        movie.title = request.POST.get('title')
        print(movie.title)
        
        movie.released_year = request.POST.get('released_year')
        movie.language = request.POST.get('language')
        movie.duration = request.POST.get('duration')
        movie.source_link = request.POST.get('source_link')
        movie.type = request.POST.get('type')
        movie.cat = request.POST.get('category_id')
        movie.slug = request.POST.get('slug')
        movie.banner = request.POST.get('banner')
        movie.catagory_id = request.POST.get('category_id')
        
        movie.save()
        return redirect("/movies/")
    return render(request, "movie_edit.html", context)
    
# def hello_view(request):
#     context = {
#         'title':"Uzmovie.com saytiga xush kelibsiz!!!",
#         'movie_img':[
#             "http://images.vfl.ru/ii/1646073225/a817377d/38259143.jpg",
#             "http://images.vfl.ru/ii/1585336235/4bca1a95/30020688.jpg",
#             "http://images.vfl.ru/ii/1646153646/437c3d50/38273113.jpg",
#             "http://images.vfl.ru/ii/1645802067/652887ff/38220376.jpg"
#         ]
#     }
#     return render(request, 'homepage.html', context)
#     # return HttpResponse(html)
    
  
    # movie.title= "5"
    # print(movie.title)
    # movie.save()
    # print(movie.title)
    # movie = Movie(title=movie.title,
    #                       language=movie.lan,
    #                       duration=movie.duration,
    #                       released_year=movie.released_year,
    #                       source_link=movie.source_link,
    #                       type=movie.type,
    #                       category_id=movie.cat,
    #                       banner=movie.ban,
    #                       slug=movie.slug)