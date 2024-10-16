# NOTE: THIS REPO IS NOW ARCHIVED AND WILL NOT BE UPDATED AFTER 10/16. PLEASE CLONE THE NEW STUDENT REPO: https://github.com/uchicago-harris-dap/student30538


# PPHA 30538: Data and Programming in Python
## Fall 2024
## University of Chicago Harris School of Public Policy
## Peter Ganong and Maggie Shi

Welcome to the repository for PPHA 30538: Data and Programming in Python. 

## Repository Structure

Each lecture will have its own folder with the following materials:
- **Quarto code**: `.qmd` files that are the source of the lecture slides.
- **Supporting materials**: Any images, data files, or external resources referenced in the slides.
- **Slides**: knitted PDF or HTML files that contain the slides used during the lecture.

Each problem set will also have its own folder.

## Branches

There are two branches in this repository:
- **`main`**: This branch contains `qmd` of slides **without** answers to the in-class exercises and do-pair-shares.
- **`after_lecture`**: This branch contains the knitted slides **with** the answers included.

### Workflow

1. **Before the lecture**: 
   - Switch to the `main` branch.
   - Pull the latest version of the slides.
   
2. **After the lecture**: 
   - Switch to the `after_lecture` branch.
   - Pull the version of the slides with answers.

## Getting Started

### GitHub Desktop Instructions

1. **Ensure you are logged in to GitHub**:
   - Open GitHub Desktop.
   - Navigate to `File > Options` (on Windows) or `GitHub Desktop > Preferences` (on Mac).
   - Check the `Accounts` tab to make sure you're logged into your GitHub account.

2. **Clone the repository**:
   - Open GitHub Desktop.
   - Click on `File > Clone Repository`.
   - Enter the repository URL: https://github.com/uchicago-harris-dap/ppha30538_fall2024.
   - Choose the location on your computer to save the repository and click `Clone`.

3. **Switch between branches**:
   - In GitHub Desktop, go to the `Current Branch` menu at the top of the window.
   - Select either `main` or `after_lecture` from the dropdown list to switch branches.

4. **Check which branch you're on**:
   - The currently active branch is displayed at the top of the window in GitHub Desktop under the `Current Branch` menu.

5. **Pull the latest changes**:
   - Click `Fetch origin` (if updates are available, it will say `Pull origin`). This will download the most recent changes for the branch you are on.

### Git Command Line Instructions

1. **Ensure you are logged in to GitHub**:
   - In your browser, navigate to [GitHub](https://github.com) and log in to your account.

2. **Clone the repository**:
   - Open your terminal.
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/uchicago-harris-dap/ppha30538_fall2024
     ```
   - Navigate into the cloned repository folder:
     ```bash
     cd ppha30538_fall2024
     ```

3. **Switch branches**:
   - To switch to the `main` branch:
     ```bash
     git checkout main
     ```
   - To switch to the `after_lecture` branch:
     ```bash
     git checkout after_lecture
     ```

4. **Check the current branch**:
   - Run the following command to see which branch you're on:
     ```bash
     git branch
     ```
   - The active branch will have an asterisk (*) next to it.

5. **Pull the latest changes**:
   - To fetch and pull the latest changes from the current branch:
     ```bash
     git pull
     ```

Feel free to reach out via EdDiscussion if you have any questions or run into any issues. Happy coding!
