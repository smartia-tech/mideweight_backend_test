import pydantic
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from data_sources.views import PosseDetail, PosseList


class ReqPosse(pydantic.BaseModel):
    label: str


class RespPosse(ReqPosse):
    id: int


class ReqGateway(pydantic.BaseModel):
    label: str
    location: str
    oauth2_client_id: str
    serial_number: str
    posse: int


class TestApi(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        cls.req_posse_1 = ReqPosse(label='first posse label')
        cls.resp_posse_1 = RespPosse(label='first posse label', id=1)
        cls.req_posse_2 = ReqPosse(label='second posse label')
        cls.resp_posse_2 = RespPosse(label='second posse label', id=2)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        PosseList.as_view()(self.factory.post(PosseList.url(),
                                              self.req_posse_1.dict()))
        PosseList.as_view()(self.factory.post(PosseList.url(),
                                              self.req_posse_2.dict()))

    def tearDown(self):
        pass

    def test_posse_list(self):
        get_request = self.factory.get(PosseList.url(), {})
        get_resp = PosseList.as_view()(get_request)
        # return list of 2
        self.assertEqual(len(get_resp.data), 2)
        req_posse = ReqPosse(label='third posse label')
        resp_posse = RespPosse(label='third posse label', id=3)
        post_resp = PosseList.as_view()(self.factory.post(
            PosseList.url(), req_posse.dict()))
        # adding a third posse
        self.assertEqual(post_resp.data['label'], resp_posse.label)
        self.assertEqual(post_resp.data['id'], resp_posse.id)

    def test_posse_detail(self):
        # get
        get_request = self.factory.get(PosseDetail.url(self.resp_posse_2.id))
        get_resp = PosseDetail.as_view()(get_request, pk=self.resp_posse_2.id)
        self.assertEqual(get_resp.data['label'], self.resp_posse_2.label)
        # put
        new_label = 'new label'
        put_request = self.factory.put(PosseDetail.url(self.resp_posse_2.id),
                                       {'label': new_label})
        put_resp = PosseDetail.as_view()(put_request, pk=self.resp_posse_2.id)
        self.assertEqual(put_resp.data['label'], new_label)
        # delete
        delete_request = self.factory.delete(
            PosseDetail.url(self.resp_posse_2.id))
        delete_resp = PosseDetail.as_view()(delete_request,
                                            pk=self.resp_posse_2.id)
        get_request = self.factory.get(PosseList.url(), {})
        get_resp = PosseList.as_view()(get_request)
        self.assertEqual(len(get_resp.data), 1)
