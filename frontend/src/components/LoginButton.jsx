import { GoogleLogin } from 'react-google-login';
import { useDispatch } from 'react-redux'
import { setToken } from '../features/tokenSlice'

const LoginButton = (props) => {
  const dispatch = useDispatch()

  const responseGoogle = (response) => {
    console.log(response)
    if(response.tokenId){
      dispatch(setToken(response.tokenId))
      props.handleLogin()
    }
  }

  return (
    <div className="justify-content-righ">
      <GoogleLogin
        clientId="276183118823-rhbiphepa9bs3bsi04mliqn5inbp5nle.apps.googleusercontent.com"
        render={renderProps => (
          <button className="btn btn-outline-info btn-md px-4 me-sm-3 fw-bold" onClick={renderProps.onClick}>Login</button>
        )}
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  )
}

export default LoginButton