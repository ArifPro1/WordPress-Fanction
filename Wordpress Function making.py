def wp_paragraph(p_text):
    code = f"<!--wp:paragraph--><p>{p_text}</p><!--wp:paragraph-->"
    return code

demo = "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available."

p = wp_paragraph(demo)
print(p)