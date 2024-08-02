const apiBaseUrl = process.env.REACT_APP_API_ENDPOINT;

// Define and export endpoints
const appEndpoints = {
  login: `/login/`,
  dashboard: `/dashboard/`,
};

const apiEndpoints = {
  login: `${apiBaseUrl}/api/v1/login/`,
  logout: `${apiBaseUrl}/api/v1/logout/`,
  signup: `${apiBaseUrl}/api/v1/signup/`,
  ruleEngine: `${apiBaseUrl}/api/v1/rule-chain/generate/`,
};

export { appEndpoints, apiEndpoints };
