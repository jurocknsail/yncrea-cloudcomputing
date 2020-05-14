# Getting started with Github

The goal of this exercise is to **upload** your current progress into a {==version control system==}.

For this course, we are using *Github* as our platform. 

---

## Repository

1. Sign Up to Github.com
1. Install git on your workstation (with any package manager or from their [website](https://git-scm.com/downloads))
1. From the Github web interface, create a new repository with the name `yncrea-cloudcomputing-microservice`. 
    It will serve as the base for the following days and all changes will be stored here.
1. Follow the [instructions](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) on how to add existing source code into your newly created repository. 
    Perform the indicated steps at the root of your project folder.  
    
    !!! info
        A good practice is to {==**separate the micro services and the infra**==}.  
        From now on, each micro service will have its own git repository.  
        With the same logic, the infra as code will also have its own repo.
        
1. Push your source code into your repository

    !!! info
        [Github Guides](https://guides.github.com/) is a good source of basic knowledge. Check it out :)

---

Once this is done, you can take the remaining time and get familiar with the Gitflow best practice [here](https://guides.github.com/introduction/flow/).

!!! info
    Ideally, for future labs you will create a new [branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) for every exercise and merge it to the Git master through a "Pull Request".
    Go ahead and prepare your first branch for the next exercise.

!!! success
    Congratulation, you have your own Github repository, and you are part of the Open Source community !