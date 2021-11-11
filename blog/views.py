from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User
from django.contrib import messages
from .models import BlogPost, BlogComment
from .templatetags import extras

# Create your views here.
def bloghome(request):
    posts = BlogPost.objects.all()
    blogs = {
        'posts': posts,
    }
    print(posts)
    return render(request, 'blog/home.html', blogs)


def blogpost(request, slug):
    # returns required blog as per the slug
    post = BlogPost.objects.get(slug=slug)
    post.views = post.views + 1
    post.save()
    # to return all root(non-reply) cmnts associated with this blogpost
    cmnts = BlogComment.objects.filter(post=post,parent=None)
    # to return all replies i.e. cmnts with some valid parent field
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replydict = {}
    for reply in replies:
        if reply.parent.comment_id not in replydict.keys() :
            replydict[reply.parent.comment_id] = [reply]
        else:
            replydict[reply.parent.comment_id].append(reply)
    total = len(cmnts)
    thank = False
    if len(cmnts) == 0:
        thank = True
    else:
        cmnts = reversed(list(cmnts))
    params = {'post': post, 'cmnts': cmnts, 'thank': thank, 'total': total, 'replydict':replydict}
    return render(request, 'blog/blogpost.html', params)


def postcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        post = request.POST['post']
        user = request.user
        parent = request.POST['parent']

        page = BlogPost.objects.get(post_id=post)
        slug = page.slug

        # checks
        if len(comment) < 10:
            messages.error(request, 'You cannot post an empty comment')
            return redirect(f'/blog/{slug}')
        else:
            # sending BlogPost obj instead of post_id
            if parent != '':
                parent = BlogComment.objects.get(comment_id=parent)
                cmnt = BlogComment(comment=comment, user=user, post=page,parent=parent)
                messages.success(request, 'Your reply has been posted successfully')
            else:
                cmnt = BlogComment(comment=comment, user=user, post=page,parent=None)
                messages.success(request, 'Your comment has been posted successfully')
            cmnt.save()
    return redirect(f'/blog/{slug}')
