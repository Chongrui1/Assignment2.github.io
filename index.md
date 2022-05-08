## Assignment2.Slope map of algorithm D8

Using the [editor on GitHub](https://github.com/Chongrui1/Assignment2.github.io/edit/gh-pages/index.md) to maintain and preview the content.

GitHub Pages will run [Jekyll](https://jekyllrb.com/) to reconstruct the content in the website, from the content in the Markdown files.

### Description of programming content:

This is a project of the build of the slope map via using the D8 algorithm, this project is about output map of the maximum slope via using the original image and the associated programming idea of calculating the maximum slope value. The creation of this project's base is the application of "Pycharm" and external plugin "Anaconda".

### How to run it?:
Users can run it from pycharm application, and only need to run this model, all the related information can be downloaded, and all the maximum output map can be created.The project is mainly intended to simulate the offer to manufacturers, in order to provide a small project of the program for the production of maps of the maximum slope.


### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block
# Header 1
## This is the part of the core algorithm:

  for i in range(len(data)):
        for j in range(len(data[0])):
            #get slope
            S = data[i][j] - data[i + 1][j] if i != Xsize-1 else -1
            SE = (data[i][j] - data[i + 1][j + 1]) / sqrt(2) if(i != (Xsize - 1) and j != (Ysize - 1))
            ...


[Link](url) and ![Image](src)
```

You can find more details via the[Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes
[repository settings](https://github.com/Chongrui1/Assignment2.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

