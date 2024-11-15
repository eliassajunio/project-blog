from typing import Any
from django.http import Http404
from blog.data import posts
from django.views.generic import TemplateView

# View da página principal.
class HomePageView(TemplateView):
    template_name = "global/index.html"

    # Define diferentes contexts para incluir na página.
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Define o context que será o nome da página.
        context["page_name"] = "Home"
        
        return context
    
# View da página do blog.
class BlogPageView(TemplateView):
    template_name = "global/blog.html"

    # Define diferentes contexts para incluir na página.
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Define o context que será o nome da página.
        context["page_name"] = "Blog"
        # Busca os posts que estão no arquivo data.
        context["posts"] = posts

        return context

# View de cada post separado.
class PostPageView(TemplateView):
    template_name = "global/singlepost.html"

    # Define diferentes contexts para incluir na página.
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Busca o post com base no ID.
        post_id = kwargs.get("id")
        post = next((post for post in posts if post["id"] == post_id), None)

        # Se não encontrar o post, levanta um erro 404.
        if not post:
            raise Http404("Post não encontrado.")

        post["title"] = post["title"].title()
        context["post"] = post

        return context
