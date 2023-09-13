class Post:
    index = ""
    title = ""
    author = ""
    img = ""
    slug = ""
    content = ""
    excerpt = ""
    link = ""
    categories = []
    
    def __init__(self, index=str|int, title=str, author=str, img=str, slug=str, content=str, excerpt=str, link=str, categories=str|list[str]):
        self.index = index
        self.title = title
        self.author = author
        self.img = img
        self.slug = slug
        self.content = content
        self.excerpt = excerpt
        self.link = link
        self.categories = categories
        
    def __str__(self):
        details = ""
        details += f"ID            : {self.index}\n"
        details += f"Título        : {self.title}\n"
        details += f"Autor         : {self.author}\n"
        details += f"URL da Imagem : {self.img}\n"
        details += f"SLUG          : {self.slug}\n"
        details += f"Conteúdo      : {self.content}\n"
        details += f"Excerpt       : {self.excerpt}\n"
        details += f"Link          : {self.link}\n"
        details += f"Categorias    : {self.categories}\n"
        
        return details