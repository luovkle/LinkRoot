import { AiOutlineSearch } from "react-icons/ai"

export const Search = () => {
  return (
    <>
      <input 
        className="flex border-1 focus:outline-none text-black bg-white px-3 rounded-l-3xl 
          sm:duration-300 sm:h-6 sm:text-sm  md:text-md md:h-8 lg:text-xl"
        type="search" name="search" placeholder="Search" />
      <button 
        type="submit" 
        className="m-0 px-2 py-0 bg-white/50 backdrop-blur-sm rounded-r-3xl
        rounded-l-none hover:bg-gray-200"
        >
        <AiOutlineSearch size={20} />
      </button>
    </>
  )
}
