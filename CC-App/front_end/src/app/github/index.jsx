import axios from 'axios';

const githubToken = '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'; 
const repoOwner = 'fitsumM12'; 
const repoName = 'Cervical Cancer-Repo'; 

export const baseURL = `https://api.github.com/repos/${repoOwner}/${repoName}/contents`;

const headers = {
  Authorization: `token ${githubToken}`
};

export const addImage = async (filePath, fileContent) => {
  const url = `${baseURL}/${filePath}`;
  const data = {
    message: 'Add image',
    content: fileContent
  };
  try {
    const response = await axios.put(url, data, { headers });
    return response.data;
  } catch (error) {
    throw new Error('Error adding image: ' + error.message);
  }
};

export const updateImage = async (filePath, fileContent, sha) => {
  const url = `${baseURL}/${filePath}`;
  const data = {
    message: 'Update image',
    content: fileContent,
    sha
  };
  try {
    const response = await axios.put(url, data, { headers });
    return response.data;
  } catch (error) {
    throw new Error('Error updating image: ' + error.message);
  }
};

export const deleteImage = async (filePath, sha) => {
  const url = `${baseURL}/${filePath}`;
  const data = {
    message: 'Delete image',
    sha
  };
  try {
    const response = await axios.delete(url, { headers, data });
    return response.data;
  } catch (error) {
    throw new Error('Error deleting image: ' + error.message);
  }
};
