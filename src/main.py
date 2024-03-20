import os, shutil

from htmlnode import extract_title, markdown_to_html_node, markdown_to_blocks, block_to_block_type

def copy_contents(source_dir, target_dir):
    if os.path.exists(source_dir) is False:
        raise ValueError(f"Source directory \"{source_dir}\" does not exist")
    if os.path.exists(target_dir) is True:
        shutil.rmtree(target_dir)
        # print(f"Removing directory \"{target_dir}\" and all of its contents")
    os.mkdir(target_dir)
    # print(f"Making empty directory \"{target_dir}\"")

    items = os.listdir(source_dir)
    for item in items:
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, target_dir)
            # print(f"Copying file \"{item}\" from \"{source_dir}\" to \"{target_dir}\"")
        elif os.path.isdir(item_path):
            new_target_dir = os.path.join(target_dir, item)
            # print(f"Calling copy contents on src = \"{item_path}\" and target = \"{new_target_dir}\"")
            copy_contents(item_path, new_target_dir)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_contents = ""
    template_contents = ""
    f = open(from_path)
    markdown_contents = f.read()
    t = open(template_path)
    template_contents = t.read()
    if markdown_contents == "":
        raise ValueError("Invalid markdown contents")
    if template_contents == "":
        raise ValueError("Invalid template")

    title = extract_title(markdown_contents)
    top_htmlnode = markdown_to_html_node(markdown_contents)
    
    generated_html = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", top_htmlnode.to_html())

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as h:
        h.write(generated_html)

    f.close()
    t.close()

def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    items = os.listdir(content_dir_path)
    for item in items:
        item_path = os.path.join(content_dir_path, item)
        if os.path.isfile(item_path):
            dest_file_path = os.path.join(dest_dir_path, item.removesuffix(".md") + ".html")
            generate_page(item_path, template_path, dest_file_path)
        elif os.path.isdir(item_path):
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dest_dir_path)
        

def main():

    try:
        generate_pages_recursive("content", "template.html", "public")
    except OSError as e:
        print(e)

    # copy_contents("static", "public")
    '''
    with open("content/index.md") as f:
        markdown_contents = f.read()
        # markdown_blocks = markdown_to_blocks(markdown_contents)
        # print(markdown_blocks[0])
        # print(block_to_block_type(markdown_blocks[0]))
        print(markdown_to_html_node(markdown_contents))
    '''
    print("main")

main()
