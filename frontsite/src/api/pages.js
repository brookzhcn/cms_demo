import request from '@/plugin/axios'

export function getPagesList(data) {
    return request({
        url: '/pages/',
        method: 'get',
        data
    })
}