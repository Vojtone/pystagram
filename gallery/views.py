from django.shortcuts import render, get_object_or_404
from .models import User, Photo, Comment


def index(request):
    all_users = User.objects.all()
    return render(request, 'gallery/index.html', {'all_users': all_users})


def grid(request, user_username):
    user = get_object_or_404(User, username=user_username)
    return render(request, 'gallery/grid.html', {'user': user})


def liked(request, user_username):
    user = get_object_or_404(User, username=user_username)
    try:
        selected_photo = user.photo_set.get(id=request.POST['photo'])
    except (KeyError, Photo.DoesNotExist):
        return render(request, 'gallery/grid.html', {
            'user': user,
            'error_message': "You did not select any photo"
        })
    else:
        selected_photo.liked = not selected_photo.liked
        selected_photo.save()
        return render(request, 'gallery/grid.html', {'user': user})


def detail(request, user_username, photo_id):
    user = get_object_or_404(User, username=user_username)
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'gallery/detail.html', {'user': user, 'photo': photo})


def commented(request, user_username, photo_id):
    user = get_object_or_404(User, username=user_username)
    photo = get_object_or_404(Photo, id=photo_id)

    # Due to lack of the user authentication the author of comment is the author of the photo for now.
    comment = Comment(author=user, photo=photo, content=request.POST['comment'])
    comment.save()
    return render(request, 'gallery/detail.html', {'user': user, 'photo': photo})
