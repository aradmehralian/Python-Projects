# Random Password Generator
This project implements three types of password generators:

1. **Pin Code Generator**: Generates a numeric PIN code of a specified length.

2. **Random Password Generator**: Generates a random password of a specified length, including uppercase letters, lowercase letters, digits, and special characters.

3. **Memorable Password Generator**: Generates a memorable password with a specified number of words from a list of words.


## Project Structure

- `data/`
    - `sample words.txt`: A sample list of words used for generating memorable passwords.

- `scripts/`
    - `build_word_list.py`: A script to build a words list from NLTK's words corpus. Saves the list to `data/sample words.txt`.

- `src/`:
    - `password_generator.py`: Contains the implementation of the password generators.

- `utils/`
    - `character.py`: Contains alphabet, digits, and special characters used in the password generation.
    - `data_loader.py`: Loads the words list from `data/sample words.txt"`.
    - `pools.py`: Builds the character pools for the password generators.

- `main.py`: The test script to run the password generators.
- `requirements.txt`: Contains the required packages for the project.

## Requirements
- python 3.9 or higher
- nltk 3.9 or higher

## How to Run

1. Clone the repository to your local machine using the command below:
   ```bash
   git clone https://github.com/aradmehralian/Python-Projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd "Level I/ Password Generator"
   ```

3. Install the required packages:
    - using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    - or using `conda`:
    ```bash
    conda install --file requirements.txt
    ```

4. If you're running the project for the first time, you need to build the `sample words.txt` file:

    - from the project's root directory run:
    ```bash
    python scripts/build_word_list.py
    ```
This will download NLTK's words corpus and create the `sample words.txt` file in `data/` directory.

**Note:** You only need to run this once.

5. Run `main.py` to see the generated passwords of each type and run the tests.

## Example Output
```bash
Generated pin code: 2280824719

Generated Random Password: '=sWgv<#T@t2'

Generated Memorable Password: Pythiad-Shopland-Papaya
```