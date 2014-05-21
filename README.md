modularized-linux-training
==========================
How we can provide linux knowhow for all interested colleagues in form of a initial training, but also provide the used material for daily work? It should be easily and immediately accessible, to be able to have a quick look when you need it!

The final idea was to provide the training materials as man pages, that we roll out on every development machine we have.

bash
----
The bash man page is huge and contains everything you always want to know about bash. Unfortunately you have to search a lot if you don't exactly know what you are looking for. This material provides flattened material about using the bash and writing good bash scripts. All paragraphs have the **same name as in the original bash man page**. So if you want to dig deeper, just search for the paragraph name in the original bash man page.

To install (e.g. on debian) clone this repository and create the desired package:

    sudo apt install ruby-ronn
    git clone https://github.com/ImmobilienScout24/modularized-linux-training.git
    cd modularized-linux-training/bash/
    make deb
    sudo dpkg -i dist/bash-essentials_1.1_all.deb
    
You can do the same for a **rpm** package. Just replace **make deb** with **make rpm** and use **rpm -i** instead of **dpkg -i**.

After the installation just type:

    man bash-essentials
    
Voilà.
    



