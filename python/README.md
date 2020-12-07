# Practical Stastics for Data Scientists

the book walsk through the statistics examples in 2 code blocks.
1) r
2) python

so i am setting up basically 3 different working environments for this repo

the first working enviornment is fairly simple
i will use rstudio, from anaconda, using environment called rstudiop

the second working environment is also fairly simple
a few py scripts using a conda environment called p36g

the last working enviornment is a bit more complicated
in windows subsystem for linux
i also have a few conda environments there, for this i will use
py36stats

one of the issues i had right off, my environment wasnt availble with jupyter notebook

so from command prompt, within the conda envionment i ran this

python -m ipykernel install --user --name=py36stats

and thats solved it.

so to get the notebooks up and running,
1) using windows command prompt, start the ubuntu command prompt
2) cd /mnt/d
2) conda activate py36stats
3) jupyter-notebook --no-browser --ip=0.0.0.0 --port=8000
4) copy the url given by the starting of jupyter with no browser , something like http://127.0.0.1:8181/?token=...
5) open windows browser and paste that in, now i am working in windows utilizing a jupyter notebook server being hosted by wsl 2.0



