# CS 410 Project Documentation

## 1) An overview of the function of the code

Our webapp performs ​text summarization for paper collections (in particular, we will develop this tool for Pubmed dataset), it will automatically find out key topics/keywords/key phrases of the papers. Those (medical) researchers who want to know what the papers are about can get a quick overview of those papers.

## 2) How the software is implemented

### Frontend && Backend

The frontend uses React and the backend uses express. And the backend is connected with python codes.

The frontend simply consists of two buttons -- "Upload" and "Submit". All the uploaded files by the user will be parsed and stored in frontend temporarily. After user click "Submit", all the parsed files will be sent to backend API and waiting for response. Once the response is returned, it renders the result.

The backend only does one thing -- call the python codes with the files from frontend. Once it receives the result from python codes, the backend will send the response to frontend.

### Python Algorithm

Python

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

Naijing Zhang (nzhang31): Python Algorithm

Zongyi Wang (zwang195): Python Algorithm
