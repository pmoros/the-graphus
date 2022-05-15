import { GoogleLogout } from 'react-google-login';
import { useDispatch } from 'react-redux'
import { setToken } from '../features/tokenSlice'

const LogoutButton = (props) => {
  const dispatch = useDispatch()
  
  const logout = () => {
    dispatch(setToken(''))
    props.handleLogin()
  }

  return (
    <div className="text-end">
      <GoogleLogout
        clientId="276183118823-rhbiphepa9bs3bsi04mliqn5inbp5nle.apps.googleusercontent.com"
        render={renderProps => (
          <button type="button" className="btn btn-outline-info btn-md px-4 me-sm-3 fw-bold" onClick={renderProps.onClick}>Logout</button>
        )}
        buttonText="Logout"
        onLogoutSuccess={logout}
      >
      </GoogleLogout>
    </div>
  )
}

export default LogoutButton