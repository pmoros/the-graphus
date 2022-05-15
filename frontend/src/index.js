import App from './App';
import { StrictMode } from "react";
import { createRoot } from 'react-dom/client';

import { Provider } from 'react-redux';
import store from './app/store'

const container = document.getElementById('root');
const root = createRoot(container); // createRoot(container!) if you use TypeScript

root.render(
  <StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>
);