// Skill Bridge - client-side JS (no build required)
const coursesUrl = './data/courses.json'
const jobsUrl = './data/jobs.json'

let courses = []
let jobs = []

// DOM refs
const tabCourses = document.getElementById('tab-courses')
const tabJobs = document.getElementById('tab-jobs')
const viewCourses = document.getElementById('view-courses')
const viewJobs = document.getElementById('view-jobs')

const courseSearch = document.getElementById('course-search')
const courseType = document.getElementById('course-type')
const coursesList = document.getElementById('courses-list')
const courseTpl = document.getElementById('course-item-tpl')

const jobSearch = document.getElementById('job-search')
const jobType = document.getElementById('job-type')
const jobsList = document.getElementById('jobs-list')
const jobTpl = document.getElementById('job-item-tpl')

// Tab switching
tabCourses.addEventListener('click', ()=>{ setActiveTab('courses') })
tabJobs.addEventListener('click', ()=>{ setActiveTab('jobs') })
function setActiveTab(t){
  if(t==='courses'){
    tabCourses.classList.add('active')
    tabJobs.classList.remove('active')
    viewCourses.classList.remove('hidden')
    viewJobs.classList.add('hidden')
  } else {
    tabJobs.classList.add('active')
    tabCourses.classList.remove('active')
    viewJobs.classList.remove('hidden')
    viewCourses.classList.add('hidden')
  }
}

// Fetch data
async function load(){
  try{
    const [cRes, jRes] = await Promise.all([fetch(coursesUrl), fetch(jobsUrl)])
    courses = await cRes.json()
    jobs = await jRes.json()
    renderCourses()
    renderJobs()
  }catch(err){
    console.error('Failed to load data', err)
    coursesList.innerHTML = '<p style="color:#b91c1c">Failed to load courses.json</p>'
    jobsList.innerHTML = '<p style="color:#b91c1c">Failed to load jobs.json</p>'
  }
}

// Render functions
function renderCourses(){
  const q = (courseSearch.value||'').trim().toLowerCase()
  const type = courseType.value
  const filtered = courses.filter(c=>{
    const matchesQ = q === '' || [c.title,c.provider,(c.tags||[]).join(' ')].join(' ').toLowerCase().includes(q)
    const matchesType = type === 'all' || (c.type && c.type.toLowerCase()===type.toLowerCase())
    return matchesQ && matchesType
  })
  if(filtered.length===0){
    coursesList.innerHTML = '<p class="muted">No courses found. Try a different query.</p>'
    return
  }
  coursesList.innerHTML = ''
  filtered.forEach(c=>{
    const node = courseTpl.content.cloneNode(true)
    node.querySelector('.title').textContent = c.title
    node.querySelector('.meta').textContent = `${c.provider} · ${c.type || 'General'} · ${c.level || ''}`
    node.querySelector('.desc').textContent = c.description
    const a = node.querySelector('.open-link')
    a.href = c.url || '#'
    a.textContent = 'Access course'
    coursesList.appendChild(node)
  })
}

function renderJobs(){
  const q = (jobSearch.value||'').trim().toLowerCase()
  const type = jobType.value
  const filtered = jobs.filter(j=>{
    const matchesQ = q === '' || [j.title,j.company,j.location].join(' ').toLowerCase().includes(q)
    const matchesType = type === 'all' || (j.type && j.type.toLowerCase()===type.toLowerCase())
    return matchesQ && matchesType
  })
  if(filtered.length===0){
    jobsList.innerHTML = '<p class="muted">No jobs found. Try a different query.</p>'
    return
  }
  jobsList.innerHTML = ''
  filtered.forEach(j=>{
    const node = jobTpl.content.cloneNode(true)
    node.querySelector('.title').textContent = j.title
    node.querySelector('.meta').textContent = `${j.company} · ${j.location} · ${j.type || ''}`
    node.querySelector('.desc').textContent = j.description
    const a = node.querySelector('.open-link')
    a.href = j.url || '#'
    a.textContent = 'View job'
    jobsList.appendChild(node)
  })
}

// Events
courseSearch.addEventListener('input', debounce(renderCourses, 180))
courseType.addEventListener('change', renderCourses)
jobSearch.addEventListener('input', debounce(renderJobs, 180))
jobType.addEventListener('change', renderJobs)

// tiny debounce
function debounce(fn, wait){
  let t
  return (...args)=>{
    clearTimeout(t)
    t = setTimeout(()=>fn(...args), wait)
  }
}

// init
load()
