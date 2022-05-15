import "../index.css"

function Home () {

  return (
    <div class="grid grid-cols-9 gap-4S">
      <div class="col-start-2 col-span-4 ...">01</div>
      <div class="col-start-1 col-end-3 ...">02</div>
      <div class="col-end-7 col-span-2 ...">03</div>
      <div class="col-start-1 col-end-7 ...">04</div>
    </div>
  )
}

export default Home