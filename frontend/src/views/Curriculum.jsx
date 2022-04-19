function Curriculum () {
  return (
    <div className="list-group">
      <label className="list-group-item d-flex gap-3">
        <input className="form-check-input flex-shrink-0" type="checkbox" value=""/>
        <span className="pt-1 form-checked-content">
          <strong>Finish sales report</strong>
          <small className="d-block text-muted">
            1:00-2:00pm
          </small>
        </span>
      </label>
      <label className="list-group-item d-flex gap-3">
        <input className="form-check-input flex-shrink-0" type="checkbox" value=""/>
        <span className="pt-1 form-checked-content">
          <strong>Weekly All Hands</strong>
          <small className="d-block text-muted">
            2:00-2:30pm
          </small>
        </span>
      </label>
      <label className="list-group-item d-flex gap-3">
        <input className="form-check-input flex-shrink-0" type="checkbox" value=""/>
        <span className="pt-1 form-checked-content">
          <strong>Out of office</strong>
          <small className="d-block text-muted">
            Tomorrow
          </small>
        </span>
      </label>
      <label className="list-group-item d-flex gap-3 bg-light">
        <input className="form-check-input form-check-input-placeholder bg-light flex-shrink-0" disabled="" type="checkbox" value=""/>
        <span className="pt-1 form-checked-content">
          <span className="w-100">Add new task...</span>
          <small className="d-block text-muted">
            Choose list...
          </small>
        </span>
      </label>
    </div>
  )
}

export default Curriculum