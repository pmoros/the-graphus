import GoogleLogin from "react-google-login";
import { Modal, Button } from 'react-bootstrap'

function LoginModal (props) {

  const responseGoogle = (response) => {
    props.handleLogin()
    console.log(response);
  }

  return (
    <>
      <Modal {...props}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <GoogleLogin
          clientId="658977310896-knrl3gka66fldh83dao2rhgbblmd4un9.apps.googleusercontent.com"
          buttonText="Continue with Google"
          onSuccess={responseGoogle}
          onFailure={responseGoogle}
          cookiePolicy={'single_host_origin'}
        />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={props.onHide}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
      
    </>
  )
}

export default LoginModal