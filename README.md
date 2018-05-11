# CS 410 Project Documentation

## 1) An overview of the function of the code

Our webapp performs ​text summarization for paper collections (in particular, we will develop this tool for Pubmed dataset), it will automatically find out key topics/keywords/key phrases of the papers. Those (medical) researchers who want to know what the papers are about can get a quick overview of those papers.

## 2) How the software is implemented

### Frontend && Backend

The frontend uses React and the backend uses express. And the backend is connected with python codes.

The frontend simply consists of two buttons -- "Upload" and "Submit". All the uploaded files by the user will be parsed and stored in frontend temporarily. After user click "Submit", all the parsed files will be sent to backend API and waiting for response. Once the response is returned, it renders the result.

The backend only does one thing -- call the python codes with the files from frontend. Once it receives the result from python codes, the backend will send the response to frontend.

### Python Algorithm

#### Step 1: Preprocessing

First of all, since we have found that there are lots of abbreviations in the pubmed data and we need to further combine phrase abbreviation and its full spelling in the algorithm, such as matrix metallopeptidase 9 (MMP9), we handle this problem at the beginning of the tokenization part by modifying the content of the original file that users submit.

Then we transfer all tokens to lower case and remove stop words from them.


#### Step 2: Term Frequency (TF)

For term frequency, we perform the following recursion algorithm:

Base case: for terms that contain only 1 word, we define it's level 1 and simply counts their frequencies in all the documents.

Recursive call: for phrases that contain i words, we check all frequent phrases at level i-1 which occur more times than a threshold, and add both the preceding and the following word of each frequent phrase at level i-1 to that phrase and form phrases contain i words. We then count the frequency of newly formed phrases in all the documents and proceed to next level until at level i there are no more frequent phrases.


#### Step 3: Incorporate MI, IDF

We then iterate through all phrases we got and for a phrase we find all possible splits and check MI (Mutual Information) and remove the splitted phrases pair whose MI is larger than a predefined threshold. And then we add IDF (Inverse Document Frequency) weighting and remove phrases whose IDF are too small.


#### Step 4: Final pruning based on word length & Frequency

Sort the entire array based on frequency first and on word length to break the tie when necessary (which happens frequently). And then choose the top k phrases to return to frontend to be displayed.



## 3) How to install and run

### Install

```bash
npm install
```

### Run

```bash
npm start
```

### Use

Open browser and go to http://localhost:5000/.

### Build Frontend

```bash
npm run build
```

### Install Backend and Frontend for development

```bash
npm run ins
```

### Development

```bash
npm run dev
```

## 4) Brief description of contribution of each team member

Mingze Xiao (mxiao6): Frontend && Backend

Naijing Zhang (nzhang31): Python Algorithm: Preprocessing, Tokenization, TF weighting.

Zongyi Wang (zwang195): Python Algorithm: Abrreviation Handling, MI, IDF weighting, Final pruning.
