def wp_p(p_text):
    code = f"<!--wp:paragraph--><p>{p_text}</p><!--/wp:paragraph-->"
    return code

# demo_text = "Here is paragraph test for a blog post Here is paragraph test for a blog post"
#
# p = wp_paragraph(demo_text)
#
# print(p)

def h2(heading_text):
    code = f"<!--wp:paragraph--><h2>{heading_text}</h2><!--/wp:paragraph-->"
    return code
