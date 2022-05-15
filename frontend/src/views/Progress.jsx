import { useSelector } from 'react-redux'

function Progress () {
  const token = useSelector((state) => state.token.value)

  return (
    <h1>
      {`token value: ${token}`}
    </h1>
  )
}

export default Progress