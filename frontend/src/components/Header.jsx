import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import LoginButton from './LoginButton';
import LogoutButton from './LogoutButton';

const Header = () => {

  const [isLogged, setIsLogged] = useState(false)
  let navigate = useNavigate();
  const handleLogin = () => {
    setIsLogged(!isLogged)
    return navigate("/");
  }

  return (
    <header className="p-3 bg-dark text-white">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <Link className="navbar-brand text-white" to="/">
            The Graphus Project
          </Link>
          {
            isLogged ?
            <>
              <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><Link className="nav-link px-2 text-secondary" to="/Curriculum">Curriculum</Link></li>
                <li><Link className="nav-link px-2 text-secondary" to="/Progress">Progress</Link></li>
                <li><Link className="nav-link px-2 text-secondary" to="/Schedule">Schedule</Link></li>
              </ul>
              <LogoutButton handleLogin={handleLogin}/>
            </>
            :
            <>
              <div className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"></div>
              <LoginButton handleLogin={handleLogin}/>
            </>
          }
        </div>
      </div>
    </header>
  )
}

export default Header